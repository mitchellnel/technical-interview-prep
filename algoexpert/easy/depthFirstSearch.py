# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v+e) time | O(v) space
    def depthFirstSearch(self, array):
        if self is None:
            return []
        else:
            array.append(self.name)
            for child in self.children:
                child.depthFirstSearch(array)

        return array
