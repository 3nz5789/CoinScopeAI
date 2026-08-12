"""
CoinScopeAI Paper Trading — Safety-State Directory
===================================================
Single source of truth for where safety-critical state files live.

Why this exists
---------------
The kill-switch flag and paper-trading state files previously lived in
``/tmp``. That has two failure modes:

1. **Tamper surface** — ``/tmp`` is world-writable; unrelated processes can
   create or delete safety flags.
2. **Reboot amnesia** — ``/tmp`` is cleared on reboot (tmpfs on most
   distros), so an engaged kill switch silently disengaged on restart.

Resolution order for the state directory:

1. ``COINSCOPE_STATE_DIR`` environment variable (set this in the systemd
   unit — ``StateDirectory=coinscopeai`` → ``/var/lib/coinscopeai``).
2. ``~/.coinscopeai/state`` for local development.

The directory is created with mode 0700 on first use. Files written into
it by the safety layer use mode 0600 (see ``write_private_file``).
"""

import os
from pathlib import Path

STATE_DIR_ENV = "COINSCOPE_STATE_DIR"

_DEFAULT_DIR_NAME = ".coinscopeai"


def get_state_dir() -> Path:
    """Return the safety-state directory, creating it (mode 0700) if needed."""
    raw = os.environ.get(STATE_DIR_ENV, "").strip()
    base = Path(raw) if raw else Path.home() / _DEFAULT_DIR_NAME / "state"
    base.mkdir(parents=True, exist_ok=True, mode=0o700)
    if not raw:
        # Best-effort tightening for the default dir; never fail on this.
        try:
            os.chmod(base, 0o700)
        except OSError:
            pass
    return base


def get_kill_flag_path() -> Path:
    """Path of the persistent kill-switch flag."""
    return get_state_dir() / "kill_switch.flag"


def write_private_file(path: Path, content: str) -> None:
    """Write a file with owner-only permissions (0600) from creation.

    Uses os.open with an explicit mode so the file is never briefly
    world-readable between write and chmod.
    """
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        with os.fdopen(fd, "w") as f:
            f.write(content)
    except Exception:
        raise
