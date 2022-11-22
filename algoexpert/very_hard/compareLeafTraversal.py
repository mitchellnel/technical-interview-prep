# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n + m) time | O(h1 + h2) space
def compareLeafTraversal_preorderTrav(tree1, tree2):
    tree1_stack = [tree1]
    tree2_stack = [tree2]

    while len(tree1_stack) > 0 and len(tree2_stack) > 0:
        tree1_leaf = get_next_leaf(tree1_stack)
        tree2_leaf = get_next_leaf(tree2_stack)

        if tree1_leaf.value != tree2_leaf.value:
            return False

    return len(tree1_stack) == 0 and len(tree2_stack) == 0


def get_next_leaf(traversal_stack):
    curr = traversal_stack.pop()

    while not is_leaf(curr):
        if curr.right is not None:
            traversal_stack.append(curr.right)
        if curr.left is not None:
            traversal_stack.append(curr.left)

        curr = traversal_stack.pop()

    return curr


# O(n + m) time | O(max(h1, h2)) space
def compareLeafTraversal_linkedList(tree1, tree2):
    tree1_leaf_ll, _ = create_leaf_ll(tree1)
    tree2_leaf_ll, _ = create_leaf_ll(tree2)

    while tree1_leaf_ll is not None and tree2_leaf_ll is not None:
        if tree1_leaf_ll.value != tree2_leaf_ll.value:
            return False

        tree1_leaf_ll = tree1_leaf_ll.right
        tree2_leaf_ll = tree2_leaf_ll.right

    return tree1_leaf_ll is None and tree2_leaf_ll is None


def create_leaf_ll(node, head=None, prev=None):
    if node is None:
        return head, prev

    if is_leaf(node):
        if prev is None:
            head = node
        else:
            prev.right = node

        prev = node

    left_head, left_prev = create_leaf_ll(node.left, head, prev)
    return create_leaf_ll(node.right, left_head, left_prev)


def is_leaf(node):
    return node.left is None and node.right is None


def is_leaf(node):
    return node.left is None and node.right is None
