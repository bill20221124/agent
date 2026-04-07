from src.main import load_config


def test_load_config_defaults():
    cfg = load_config()
    assert cfg.app_env
    assert cfg.log_level
