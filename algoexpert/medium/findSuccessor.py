# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(n) time | O(n) space
def findSuccessor_traversal(tree, node):
    traversal = inorderTraversal(tree, [])

    for idx, curr_node in enumerate(traversal):
        if idx == len(traversal) - 1:
            return None
        elif curr_node.value == node.value:
            return traversal[idx + 1]


def inorderTraversal(tree, traversal):
    if tree is not None:
        inorderTraversal(tree.left, traversal)
        traversal.append(tree)
        inorderTraversal(tree.right, traversal)

    return traversal


# O(h) time | O(1) space
def findSuccessor(tree, node):
    # inorder is left,self,right
    # so if a node has a right subtree, the node's successor
    #     must be in that right subtree - specifically the furthest left node
    # if the node doesn't have a right subtree, then the node's
    #     successor will be its parent's parent
    if node.right is not None:
        return getLeftmostChild(node.right)
    else:
        return getRightmostParent(node)


def getLeftmostChild(node):
    curr_node = node
    while curr_node.left is not None:
        curr_node = curr_node.left

    return curr_node


def getRightmostParent(node):
    curr_node = node
    while curr_node.parent is not None and curr_node.parent.right == curr_node:
        curr_node = curr_node.parent

    return curr_node.parent
