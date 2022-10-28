def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest

    curr_diff = abs(closest - target)
    this_diff = abs(tree.value - target)

    if curr_diff > this_diff:
        closest = tree.value

    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
