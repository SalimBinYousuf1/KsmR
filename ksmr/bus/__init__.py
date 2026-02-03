"""Message bus module for decoupled channel-agent communication."""

from ksmr.bus.events import InboundMessage, OutboundMessage
from ksmr.bus.queue import MessageBus

__all__ = ["MessageBus", "InboundMessage", "OutboundMessage"]
