# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


# O(n) time | O(h) space
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    left_subtree_info = getTreeInfo(tree.left)
    right_subtree_info = getTreeInfo(tree.right)

    longest_path_through_root = left_subtree_info.height + right_subtree_info.height
    max_diameter = max(left_subtree_info.diameter, right_subtree_info.diameter)

    curr_height = 1 + max(left_subtree_info.height, right_subtree_info.height)
    curr_diameter = max(longest_path_through_root, max_diameter)

    return TreeInfo(curr_height, curr_diameter)
