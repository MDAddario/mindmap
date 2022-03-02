class Node:

    def __init__(self, path, text=None):

        if path.count('/') == 0:
            self.name = path
            self.text = text
            self.children = []

        else:

            name, *rest = path.split('/')
            
            self.name = name
            self.text = None
            self.children = [Node('/'.join(rest), text)]

    def graft(self, path, text):

        name, *rest = path.split('/')

        for child in self.children:

            # Sliding down the tree
            if child.name == name:
                child.graft('/'.join(rest), text)

        # Spawn new branch
        else:
            self.children.append(Node(path, text))

    def read(self, path):
        pass

    def pretty(self, depth=0):

        output = '\t' * depth + self.name

        if self.children:
            output += '/\n'

        for child in self.children:
            output += child.pretty(depth + 1)
        return output
