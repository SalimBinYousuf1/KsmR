"""Configuration module for KsmR."""

from ksmr.config.loader import load_config, get_config_path
from ksmr.config.schema import Config

__all__ = ["Config", "load_config", "get_config_path"]
