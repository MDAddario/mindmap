import pickle as pkl
from pathlib import Path
from contextlib import contextmanager


file_db = Path(__file__).parent.resolve()/"database.pkl"


@contextmanager
def database():
    
    # Load the db from file
    try:
        with file_db.open('rb') as f:
            db = pkl.load(f)
    except FileNotFoundError:
        db = {}

    # Yield the DB for edits
    try:
        yield db

    # Update the db's file
    finally:
        with file_db.open('wb') as f:
            pkl.dump(db, f)
