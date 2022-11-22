# O(nlog(n)) time | O(d) space
def allKindsOfNodeDepths(root):
    if root is None:
        return 0
    return (
        all_kinds_of_node_depths_helper(root, 0)
        + allKindsOfNodeDepths(root.left)
        + allKindsOfNodeDepths(root.right)
    )


def all_kinds_of_node_depths_helper(node, curr_depth):
    if node is None:
        return 0

    left_depth_sum = all_kinds_of_node_depths_helper(node.left, curr_depth + 1)
    right_depth_sum = all_kinds_of_node_depths_helper(node.right, curr_depth + 1)

    return left_depth_sum + right_depth_sum + curr_depth


class TreeInfo:
    def __init__(self, size, depth_sum, all_depth_sum):
        self.size = size
        self.depth_sum = depth_sum
        self.all_depth_sum = all_depth_sum


# O(n) time | O(d) space
def allKindsOfNodeDepths(root):
    return get_tree_info(root).all_depth_sum


def get_tree_info(node):
    if node is None:
        return TreeInfo(0, 0, 0)

    left_info = get_tree_info(node.left)
    right_info = get_tree_info(node.right)

    size = left_info.size + right_info.size + 1

    left_depth_sum = left_info.depth_sum + left_info.size
    right_depth_sum = right_info.depth_sum + right_info.size
    depth_sum = left_depth_sum + right_depth_sum

    all_depth_sum = depth_sum + left_info.all_depth_sum + right_info.all_depth_sum

    return TreeInfo(size, depth_sum, all_depth_sum)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
