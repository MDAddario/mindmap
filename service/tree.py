"""
Data structure for mindmap manipulations
Define the nodes that will compose mind map trees
"""


class Node:
    """
    Node constructing the mind map trees

    Attributes:
        name            (str): Name of node in path
        text            (str): Text of leaf node
        children (List[Node]): All connections to child nodes
    """

    def __init__(self, names=("root",), text=None):
        """
        Create a new node, as well as all mandatory children

        Args:
            names (collection(str)): Path split names of all children
            text              (str): Text of leaf node
        """

        self.name = names[0]

        # Final node in the path
        if len(names) == 1:
            self.text = text
            self.children = []

        # Path describes more children
        else:
            self.text = None
            self.children = [Node(names[1:], text)]

    def graft(self, names, text):
        """
        Graft a new branch to an existing tree

        Args:
            names (collection(str)): Path split names of all children
            text              (str): Text of leaf node
        """

        # Update text of existing leaf
        if len(names) == 0:
            self.text = text
            return

        # The next node still exists in the tree
        for child in self.children:
            if child.name == names[0]:
                child.graft(names[1:], text)
                break

        # Spawn new branch
        else:
            self.children.append(Node(names, text))

    def read(self, names):
        """
        Traverse tree and read text of final leaf node

        Args:
            names (collection(str)): Path split names of all children

        Returns:
            (str) text of leaf node

        Raises:
            (ValueError) path does not exist in tree
        """

        # Foudn the leaf node
        if len(names) == 0:
            return self.text

        # Traverse the tree
        for child in self.children:
            if child.name == names[0]:
                return child.read(names[1:])

        # Path does not exist
        raise ValueError

    def pretty(self, depth=0):
        """
        Pretty print entire tree

        Args:
            depth (int): distance from root node

        Returns:
            (str) formatted print of tree
        """
        # Add current node name
        output = "\t" * depth + self.name

        # Only add forward slash if leaf
        if self.children:
            output += "/\n"
        else:
            output += "\n"

        # Recurse into children
        for child in self.children:
            output += child.pretty(depth + 1)

        # Ignore linebreak for root print
        if depth == 0:
            return output[:-1]
        return output
