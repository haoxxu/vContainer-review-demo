# vContainer-review-demo

A small notes library backed by SQLite, used as the fixture for vContainer's pull request review examples. Its pull request #1 exists to be reviewed and is not meant to be merged.

## Use

```python
from notes import add_note, connect, get_note

conn = connect(":memory:")
note_id = add_note(conn, "alice", "Groceries", "eggs, milk")
print(get_note(conn, note_id))
```

Run the tests:

```sh
python3 -m unittest
```
