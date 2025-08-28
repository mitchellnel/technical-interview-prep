from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def reverse_level_order_traversal(root):
    traversal = []

    curr_depth = -1

    queue = deque([(root, 0)])
    while len(queue) > 0:
        curr_node, curr_node_depth = queue.popleft()

        # check if next node we're looking at occurs in new level
        if curr_node_depth != curr_depth:
            # add new list for this level
            traversal.insert(0, [])

            # change the curr level we're looking at
            curr_depth = curr_node_depth

        # append children to end of queue
        if curr_node.left is not None:
            queue.append((curr_node.left, curr_depth + 1))
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_depth + 1))

        # add value to the level whose list we're currently traversing
        traversal[0].append(curr_node.val)

    return traversal


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(reverse_level_order_traversal(root)))


main()
