# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    branchSumsHelper(root, 0, sums)
    return sums


def branchSumsHelper(tree, running_sum, sums):
    if tree is None:
        return

    running_sum += tree.value

    if tree.left is None and tree.right is None:
        sums.append(running_sum)

    branchSumsHelper(tree.left, running_sum, sums)
    branchSumsHelper(tree.right, running_sum, sums)
