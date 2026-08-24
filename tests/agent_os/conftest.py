import pytest


@pytest.fixture(autouse=True)
def isolated_safety_state(
    monkeypatch: pytest.MonkeyPatch, tmp_path: pytest.TempPathFactory
) -> None:
    state_dir = tmp_path / "coinscope-state"
    monkeypatch.setenv("COINSCOPE_STATE_DIR", str(state_dir))
