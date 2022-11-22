# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def flattenBinaryTree_traversal(root):
    inorder = inorder_traversal(root, [])

    for i in range(0, len(inorder) - 1):
        inorder[i].right = inorder[i + 1]
        inorder[i + 1].left = inorder[i]

    return inorder[0]


def inorder_traversal(tree, array):
    if tree is not None:
        inorder_traversal(tree.left, array)
        array.append(tree)
        inorder_traversal(tree.right, array)

    return array


# O(n) time | O(d) space
def flattenBinaryTree(root):
    leftmost_node, _ = flatten_binary_tree_helper(root)
    return leftmost_node


def flatten_binary_tree_helper(node):
    if node.left is None:
        leftmost = node
    else:
        left_subtree_leftmost, left_subtree_rightmost = flatten_binary_tree_helper(
            node.left
        )

        connect_nodes(left_subtree_rightmost, node)

        leftmost = left_subtree_leftmost

    if node.right is None:
        rightmost = node
    else:
        right_subtree_leftmost, right_subtree_rightmost = flatten_binary_tree_helper(
            node.right
        )

        connect_nodes(node, right_subtree_leftmost)

        rightmost = right_subtree_rightmost

    return leftmost, rightmost


def connect_nodes(left, right):
    left.right = right
    right.left = left
