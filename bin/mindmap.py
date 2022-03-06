from tree import Node

# Registry to store all the trees
registry = {}


def create_map(identity):

    # Make sure ID is new
    if identity in registry:
        return f"ID \"{identity}\" already has a mind map.", 400

    # Add the ID to our registry
    registry[identity] = Node()
    return 'Mind map creation successful.'


def add_leaf(identity, path, text):

    # Graft new leaf to tree
    try:
        registry[identity].graft(path.split('/'), text)
        return 'Mind map leaf addition successful.'

    # ID not found
    except KeyError:
        return f"ID \"{identity}\" does not have a mind map.", 400
        

def read_leaf(identity, path):

    # Traverse the path
    try:
        return registry[identity].read(path.split('/'))

    # ID not found
    except KeyError:
        return f"ID \"{identity}\" does not have a mind map.", 400


def read_tree(identity):
    
    # Print the whole tree
    try:
        return registry[identity].pretty()

    # ID not found
    except KeyError:
        return f"ID \"{identity}\" does not have a mind map.", 400
