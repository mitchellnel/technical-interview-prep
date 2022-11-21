# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        visited = []

        while queue:
            curr = queue.pop(0)
            visited.append(curr)

            array.append(curr.name)

            if len(curr.children) > 0:
                queue += curr.children

        return array
