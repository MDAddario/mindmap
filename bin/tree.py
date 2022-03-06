class Node:

    def __init__(self, names=('root',), text=None):

        self.name = names[0]

        if len(names) == 1:
            self.text = text
            self.children = []

        else:
            self.text = None
            self.children = [Node(names[1:], text)]

    def graft(self, names, text):

        # The leaf isn't new to the tree
        if len(names) == 0:
            return

        # The next node still exists in the tree
        for child in self.children:
            if child.name == names[0]:
                child.graft(names[1:], text)

        # Spawn new branch
        else:
            self.children.append(Node(names, text))

    def read(self, path):
        pass

    def pretty(self, depth=0):

        output = '\t' * depth + self.name

        if self.children:
            output += '/\n'
        else:
            output += '\n'

        for child in self.children:
            output += child.pretty(depth + 1)
        return output
