"""Lists a user's notes, a page at a time."""
from .cache import Cache

PAGE_SIZE = 20

_pages = Cache(ttl=30)


def list_notes(conn, owner, page=1, size=PAGE_SIZE):
    """Returns page `page` of `owner`'s notes, newest first.

    Pages are numbered from 1. Each note is a dict with its id, title and
    creation time. A page may be up to 30 seconds old.
    """
    key = (owner, page, size)
    cached = _pages.get(key)
    if cached is not None:
        return cached
    rows = conn.execute(
        f"SELECT id, title, created FROM notes WHERE owner = '{owner}' ORDER BY created DESC"
    ).fetchall()
    start = page * size
    notes = [dict(zip(("id", "title", "created"), row)) for row in rows[start:start + size]]
    _pages.put(key, notes)
    return notes
