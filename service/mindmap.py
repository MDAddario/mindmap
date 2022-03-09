"""
Core logic for mindmap manipulations
Defines all operations to create, expand, and read from mind maps
"""

from .tree import Node
from .persistance import database


def create_map(identity):
    """
    Create a new mind map via an ID

    Args:
        - identity (str): unique mind map ID

    Returns:
        (str) indicates success/failure of operation
    """

    # Load data into RAM
    with database() as db:

        # Make sure ID is new
        if identity in db:
            return f'ID "{identity}" already has a mind map.', 400

        # Add the ID to our db
        db[identity] = Node()
        return "Mind map creation successful."


def add_leaf(identity, path, text):
    """
    Add a leaf to an existing mind map

    Args:
        - identity (str): unique mind map ID
        - path     (str): forward-slash separated string of node names
        - text     (str): value of leaf node

    Returns:
        (str) indicates success/failure of operation
    """

    # Load data into RAM
    with database() as db:

        # Graft new leaf to tree
        try:
            db[identity].graft(path.split("/"), text)
            return "Mind map leaf addition successful."

        # ID not found
        except KeyError:
            return f'ID "{identity}" does not have a mind map.', 400


def read_leaf(identity, path):
    """
    Read a leaf from an existing mind map

    Args:
        - identity (str): unique mind map ID
        - path     (str): forward-slash separated string of node names

    Returns:
        (dict) contains 'path' and 'text' of leaf
        or
        (str) indicates failure of operation
    """

    # Load data into RAM
    with database() as db:

        # Read the text from the given leaf
        try:
            return {
                "path": path,
                "text": db[identity].read(path.split("/"))
                }

        # ID not found
        except KeyError:
            return f'ID "{identity}" does not have a mind map.', 400

        # Path doesn't exist
        except ValueError:
            return f'Path "{path}" does not exist in "{identity}" mind map.', 400


def read_tree(identity):
    """
    Read an entire existing mind map

    Args:
        - identity (str): unique mind map ID

    Returns:
        (str) pretty print of entire mind map
        or
        (str) indicates failure of operation
    """

    # Load data into RAM
    with database() as db:

        # Print the whole tree
        try:
            return db[identity].pretty()

        # ID not found
        except KeyError:
            return f'ID "{identity}" does not have a mind map.', 400
