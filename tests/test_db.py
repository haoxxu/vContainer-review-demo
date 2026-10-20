import unittest

from notes import add_note, connect, get_note


class DbTest(unittest.TestCase):
    def setUp(self):
        self.conn = connect(":memory:")

    def test_add_and_get(self):
        note_id = add_note(self.conn, "alice", "Groceries", "eggs, milk")
        note = get_note(self.conn, note_id)
        self.assertEqual((note["owner"], note["title"], note["body"]), ("alice", "Groceries", "eggs, milk"))

    def test_missing_note(self):
        self.assertIsNone(get_note(self.conn, 42))

    def test_ids_are_distinct(self):
        self.assertNotEqual(add_note(self.conn, "alice", "a", ""), add_note(self.conn, "bob", "b", ""))
