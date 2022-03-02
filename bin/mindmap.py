class Node:

    def __init__(self, path, text=None):
        pass

    def graft(self, path, text):
        pass


# Registry to store all the trees
registry = {}


def create_map(identity):

    # Make sure ID is new
    if identity in registry:
        raise ValueError(f"ID \"{identity}\" already has a mind map.")

    # Add the ID to our registry
    registry[identity] = Node('root')
    return 'Mind map creation successful.'


def add_leaf(identity, path, text):

    # Graft new leaf to tree
    try:
        registry[identity].graft(path, text)
        return 'Mind map leaf addition successful.'

    # ID not found
    except KeyError:
        raise ValueError(f"ID \"{identity}\" does not have a mind map.")
        

def read_leaf(identity, path):

    # Traverse the path
    try:
        return registry[identity].read(path)

    # ID not found
    except KeyError:
        raise ValueError(f"ID \"{identity}\" does not have a mind map.")


def read_tree(identity):
    
    # Print the whole tree
    try:
        return str(registry[identity])

    # ID not found
    except KeyError:
        raise ValueError(f"ID \"{identity}\" does not have a mind map.")
