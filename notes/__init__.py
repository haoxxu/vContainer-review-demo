"""A small notes library backed by SQLite."""
from .db import add_note, connect, get_note

__all__ = ["add_note", "connect", "get_note"]
