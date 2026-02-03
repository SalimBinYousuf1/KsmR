"""Chat channels module with plugin architecture."""

from ksmr.channels.base import BaseChannel
from ksmr.channels.manager import ChannelManager

__all__ = ["BaseChannel", "ChannelManager"]
