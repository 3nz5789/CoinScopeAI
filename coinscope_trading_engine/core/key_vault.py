"""
key_vault.py — Per-User Exchange API Key Vault (scaffold)
COI-61 | P1.5 | CoinScopeAI

Encrypted vault for user-supplied exchange API keys.
Foundation for multi-tenancy in P2; cheap to scaffold while
the engine is still single-user.

Scope (P1.5 scaffold):
  - Binance Testnet keys only
  - AES-256-GCM encryption via cryptography library
  - Keys stored in PostgreSQL `exchange_keys` table
  - Per-user isolation — no cross-user key access

NOT in scope (P2+):
  - Bybit, OKX key support (deferred)
  - Hardware security module (HSM) integration
  - Key rotation automation
"""

import os
import base64
from typing import Optional
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# ── Master encryption key ────────────────────────────────────────────────────
# Set VAULT_MASTER_KEY in .env as a 32-byte base64-encoded secret.
# Generate: python3 -c "import os,base64; print(base64.b64encode(os.urandom(32)).decode())"
# NEVER commit this key. NEVER log this key.

def _get_master_key() -> bytes:
    raw = os.environ.get("VAULT_MASTER_KEY", "")
    if not raw:
        raise RuntimeError(
            "VAULT_MASTER_KEY not set in environment. "
            "Generate with: python3 -c \"import os,base64; "
            "print(base64.b64encode(os.urandom(32)).decode())\""
        )
    return base64.b64decode(raw)


# ── Encryption / decryption ───────────────────────────────────────────────────

def encrypt_key(plaintext: str) -> str:
    """
    Encrypt an exchange API key using AES-256-GCM.

    Returns base64-encoded ciphertext with nonce prepended.
    Format: base64(nonce[12] + ciphertext)
    """
    master_key = _get_master_key()
    aesgcm = AESGCM(master_key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
    return base64.b64encode(nonce + ciphertext).decode()


def decrypt_key(encrypted: str) -> str:
    """
    Decrypt an AES-256-GCM encrypted exchange API key.

    Input: base64-encoded nonce[12] + ciphertext
    Returns: plaintext API key string
    """
    master_key = _get_master_key()
    aesgcm = AESGCM(master_key)
    raw = base64.b64decode(encrypted)
    nonce, ciphertext = raw[:12], raw[12:]
    return aesgcm.decrypt(nonce, ciphertext, None).decode()


# ── Database schema (DDL) ─────────────────────────────────────────────────────

EXCHANGE_KEYS_DDL = """
CREATE TABLE IF NOT EXISTS exchange_keys (
    id              BIGSERIAL PRIMARY KEY,
    user_id         TEXT NOT NULL,
    exchange        TEXT NOT NULL,                  -- 'binance_testnet' | 'binance' | 'bybit'
    label           TEXT NOT NULL DEFAULT 'default',
    encrypted_api_key    TEXT NOT NULL,             -- AES-256-GCM encrypted
    encrypted_api_secret TEXT NOT NULL,             -- AES-256-GCM encrypted
    is_testnet      BOOLEAN NOT NULL DEFAULT TRUE,  -- safety: default to testnet
    is_active       BOOLEAN NOT NULL DEFAULT TRUE,
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW(),
    last_verified_at TIMESTAMPTZ,                   -- last successful connectivity check

    CONSTRAINT uq_user_exchange_label UNIQUE (user_id, exchange, label)
);

CREATE INDEX IF NOT EXISTS idx_exchange_keys_user_id ON exchange_keys(user_id);
CREATE INDEX IF NOT EXISTS idx_exchange_keys_exchange ON exchange_keys(exchange);
"""


# ── Vault operations ──────────────────────────────────────────────────────────

class KeyVault:
    """
    Per-user exchange API key vault.

    Usage:
        vault = KeyVault(db_session)
        vault.store(user_id="usr_123", exchange="binance_testnet",
                    api_key="abc", api_secret="xyz")
        key, secret = vault.retrieve(user_id="usr_123", exchange="binance_testnet")
    """

    def __init__(self, db_session):
        self.db = db_session

    def store(
        self,
        user_id: str,
        exchange: str,
        api_key: str,
        api_secret: str,
        label: str = "default",
        is_testnet: bool = True,
    ) -> bool:
        """
        Encrypt and store exchange API keys for a user.

        is_testnet defaults to True — must be explicitly set False
        for live key storage (requires PCC v2 §8 sign-off first).
        """
        if not is_testnet:
            raise ValueError(
                "Live (non-testnet) key storage is not permitted during "
                "the validation phase. Set is_testnet=True or wait for "
                "PCC v2 §8 real-capital gate to open."
            )

        encrypted_key = encrypt_key(api_key)
        encrypted_secret = encrypt_key(api_secret)

        self.db.execute(
            """
            INSERT INTO exchange_keys
                (user_id, exchange, label, encrypted_api_key, encrypted_api_secret, is_testnet)
            VALUES (:user_id, :exchange, :label, :enc_key, :enc_secret, :is_testnet)
            ON CONFLICT (user_id, exchange, label)
            DO UPDATE SET
                encrypted_api_key = EXCLUDED.encrypted_api_key,
                encrypted_api_secret = EXCLUDED.encrypted_api_secret,
                updated_at = NOW()
            """,
            {
                "user_id": user_id,
                "exchange": exchange,
                "label": label,
                "enc_key": encrypted_key,
                "enc_secret": encrypted_secret,
                "is_testnet": is_testnet,
            },
        )
        self.db.commit()
        return True

    def retrieve(
        self,
        user_id: str,
        exchange: str,
        label: str = "default",
    ) -> Optional[tuple[str, str]]:
        """
        Retrieve and decrypt exchange API keys for a user.

        Returns (api_key, api_secret) or None if not found.
        """
        row = self.db.execute(
            """
            SELECT encrypted_api_key, encrypted_api_secret
            FROM exchange_keys
            WHERE user_id = :user_id
              AND exchange = :exchange
              AND label = :label
              AND is_active = TRUE
            """,
            {"user_id": user_id, "exchange": exchange, "label": label},
        ).fetchone()

        if not row:
            return None

        return decrypt_key(row[0]), decrypt_key(row[1])

    def delete(self, user_id: str, exchange: str, label: str = "default") -> bool:
        """Soft-delete (deactivate) keys for a user."""
        self.db.execute(
            """
            UPDATE exchange_keys
            SET is_active = FALSE, updated_at = NOW()
            WHERE user_id = :user_id AND exchange = :exchange AND label = :label
            """,
            {"user_id": user_id, "exchange": exchange, "label": label},
        )
        self.db.commit()
        return True

    def list_keys(self, user_id: str) -> list[dict]:
        """List active keys for a user (metadata only — no plaintext secrets)."""
        rows = self.db.execute(
            """
            SELECT exchange, label, is_testnet, created_at, last_verified_at
            FROM exchange_keys
            WHERE user_id = :user_id AND is_active = TRUE
            ORDER BY created_at DESC
            """,
            {"user_id": user_id},
        ).fetchall()

        return [
            {
                "exchange": r[0],
                "label": r[1],
                "is_testnet": r[2],
                "created_at": r[3].isoformat() if r[3] else None,
                "last_verified_at": r[4].isoformat() if r[4] else None,
            }
            for r in rows
        ]
