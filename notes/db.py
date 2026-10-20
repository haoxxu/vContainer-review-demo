"""Notes stored in SQLite."""
import sqlite3
import time


def connect(path):
    """Opens the database at `path` and creates the notes table if needed."""
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS notes ("
        "id INTEGER PRIMARY KEY, owner TEXT NOT NULL, title TEXT NOT NULL, "
        "body TEXT NOT NULL, created REAL NOT NULL)"
    )
    return conn


def add_note(conn, owner, title, body):
    """Stores a note and returns its id."""
    cur = conn.execute(
        "INSERT INTO notes (owner, title, body, created) VALUES (?, ?, ?, ?)",
        (owner, title, body, time.time()),
    )
    conn.commit()
    return cur.lastrowid


def get_note(conn, note_id):
    """Returns the note with this id as a dict, or None if there is none."""
    row = conn.execute(
        "SELECT id, owner, title, body, created FROM notes WHERE id = ?", (note_id,)
    ).fetchone()
    if row is None:
        return None
    return dict(zip(("id", "owner", "title", "body", "created"), row))
