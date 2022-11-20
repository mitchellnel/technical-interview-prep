# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, height, is_balanced):
        self.height = height
        self.is_balanced = is_balanced


# O(n) time | O(h) space
def heightBalancedBinaryTree(tree):
    if tree is None:
        return True

    return getTreeInfo(tree).is_balanced


def getTreeInfo(node):
    if node is None:
        return TreeInfo(-1, True)
    elif node.left is None and node.right is None:
        return TreeInfo(0, True)

    left_info = getTreeInfo(node.left)
    right_info = getTreeInfo(node.right)

    is_balanced = (
        left_info.is_balanced
        and right_info.is_balanced
        and abs(left_info.height - right_info.height) <= 1
    )

    height = max(left_info.height, right_info.height) + 1

    return TreeInfo(height, is_balanced)
