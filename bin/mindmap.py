from tree import Node
from persistance import database


def create_map(identity):

    # Load data into RAM
    with database() as db:

        # Make sure ID is new
        if identity in db:
            return f"ID \"{identity}\" already has a mind map.", 400

        # Add the ID to our db
        db[identity] = Node()
        return 'Mind map creation successful.'


def add_leaf(identity, path, text):

    # Load data into RAM
    with database() as db:

        # Graft new leaf to tree
        try:
            db[identity].graft(path.split('/'), text)
            return 'Mind map leaf addition successful.'

        # ID not found
        except KeyError:
            return f"ID \"{identity}\" does not have a mind map.", 400
        

def read_leaf(identity, path):

    # Load data into RAM
    with database() as db:

        # Traverse the path
        try:
            return {
                "path": path,
                "text": db[identity].read(path.split('/'))
            }

        # ID not found
        except KeyError:
            return f"ID \"{identity}\" does not have a mind map.", 400


def read_tree(identity):

    # Load data into RAM
    with database() as db:
    
        # Print the whole tree
        try:
            return db[identity].pretty()

        # ID not found
        except KeyError:
            return f"ID \"{identity}\" does not have a mind map.", 400
