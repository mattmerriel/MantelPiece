from pathlib import Path

from xdg_base_dirs import xdg_config_home, xdg_data_home

def _mantelware_directory(root: Path) -> Path:
    directory = root / "mantelware"
    directory.mkdir(exist_ok=True, parents=True)
    return directory

def config_directory() -> Path:
    """Return (and create if not exist) the application config directory."""
    return _mantelware_directory(xdg_config_home())

def config_file() -> Path:
    return config_directory() / "config.yaml"