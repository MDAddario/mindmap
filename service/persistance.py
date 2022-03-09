"""
Database for mindmap web service
Saves data locally via pickles
(yes, I know this is generally unsafe)
"""

import pickle as pkl
from pathlib import Path
from contextlib import contextmanager


# Local path to file database
file_db = Path(__file__).parent.resolve() / "database.pkl"


@contextmanager
def database():
    """
    Context manager used to access file database

    Modifications to database will be saved upon __exit__

    Usage:
    ```
    with database() as db:
        pass
    ```
    """

    # Load the db from file
    try:
        with file_db.open("rb") as f:
            db = pkl.load(f)
    except FileNotFoundError:
        db = {}

    # Yield the DB for edits
    try:
        yield db

    # Update the db's file
    finally:
        with file_db.open("wb") as f:
            pkl.dump(db, f)
