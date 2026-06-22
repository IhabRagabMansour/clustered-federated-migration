"""
Configuration loader (dot-notation access over config.yaml).
Adapted from the Gossip project for the clustered-migration module.
"""

import os
import yaml
from typing import Any, Dict


class ConfigSection:
    """Wrapper enabling dot-notation access to a nested config dict."""

    def __init__(self, section: Dict[str, Any]):
        self._section = section

    def __getattr__(self, name: str):
        if name.startswith("_"):
            return object.__getattribute__(self, name)
        if name in self._section:
            value = self._section[name]
            return ConfigSection(value) if isinstance(value, dict) else value
        raise AttributeError(f"Config section has no attribute '{name}'")

    def get(self, key: str, default: Any = None) -> Any:
        value = self._section.get(key, default)
        return ConfigSection(value) if isinstance(value, dict) else value

    def to_dict(self) -> Dict[str, Any]:
        return self._section


class Config:
    """Top-level configuration object loaded from a YAML file."""

    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        with open(config_path, "r") as f:
            self._config = yaml.safe_load(f)

    def __getattr__(self, name: str):
        if name.startswith("_"):
            return object.__getattribute__(self, name)
        if name in self._config:
            value = self._config[name]
            return ConfigSection(value) if isinstance(value, dict) else value
        raise AttributeError(f"Config has no attribute '{name}'")

    def to_dict(self) -> Dict[str, Any]:
        return self._config


# Global instance (import: from config_loader import config)
config = Config()
