# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(d) space
def rightSiblingTree(root):
    right_sibling_tree_helper(root, None, None)

    return root


def right_sibling_tree_helper(node, parent, is_left_child):
    if node is None:
        return
    left, right = node.left, node.right

    right_sibling_tree_helper(left, node, True)

    if parent is None:
        node.right = None
    elif is_left_child:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left

    right_sibling_tree_helper(right, node, False)
