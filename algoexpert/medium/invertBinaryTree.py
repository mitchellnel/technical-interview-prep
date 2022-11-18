# O(n) time | O(d) space
def invertBinaryTree(tree):
    if tree is None:
        return None

    new_left = invertBinaryTree(tree.right)
    new_right = invertBinaryTree(tree.left)

    tree.left = new_left
    tree.right = new_right

    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
