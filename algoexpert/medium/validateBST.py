# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(d) space
def validateBst(tree):
    return validateBSTHelper(tree)


def validateBSTHelper(tree, leftParent=None, rightParent=None):
    # base case
    if tree is None:
        return True

    # validation checks
    if leftParent is not None and tree.value >= leftParent.value:
        return False
    if rightParent is not None and tree.value < rightParent.value:
        return False

    # recursive step
    return validateBSTHelper(tree.left, tree, rightParent) and validateBSTHelper(
        tree.right, leftParent, tree
    )
