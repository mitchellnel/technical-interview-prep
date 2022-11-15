# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findKthLargestValueInBst_n(tree, k):
    if tree is None:
        return -1

    # do an inorder traversal, reverse, use k to index
    inorder = inorderTraversal(tree, [])

    return inorder[len(inorder) - k]


def inorderTraversal(tree, array):
    if tree is not None:
        inorderTraversal(tree.left, array)
        array.append(tree.value)
        inorderTraversal(tree.right, array)
    return array


class TreeInfo:
    def __init__(self, number_of_nodes_visited, latest_visited_value):
        self.number_of_nodes_visited = number_of_nodes_visited
        self.latest_visited_value = latest_visited_value


# O(h + k) time | O(h) space
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.latest_visited_value


def reverseInOrderTraverse(node, k, treeInfo):
    if node is None or treeInfo.number_of_nodes_visited >= k:
        return

    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.number_of_nodes_visited < k:
        treeInfo.number_of_nodes_visited += 1
        treeInfo.latest_visited_value = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)
