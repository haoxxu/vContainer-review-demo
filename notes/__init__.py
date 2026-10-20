"""A small notes library backed by SQLite."""
from .db import add_note, connect, get_note
from .listing import list_notes

__all__ = ["add_note", "connect", "get_note", "list_notes"]
