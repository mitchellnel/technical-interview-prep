# O(log(n)) time | O(1) space
def nodeDepths(root):
    return nodeDepthHelper(root, 0)


def nodeDepthHelper(node, curr_depth):
    if node is None:
        return 0

    left_depth_sum = nodeDepthHelper(node.left, curr_depth + 1)
    right_depth_sum = nodeDepthHelper(node.right, curr_depth + 1)

    return curr_depth + left_depth_sum + right_depth_sum


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
