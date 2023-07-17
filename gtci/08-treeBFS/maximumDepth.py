from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maximum_depth(root):
    if root is None:
        return 0

    max_depth = 1
    queue = deque([(root, 1)])
    while len(queue) > 0:
        curr_node, curr_node_depth = queue.popleft()

        # check if the curr node depth is a running maximum
        max_depth = max(max_depth, curr_node_depth)

        # add children to the queue
        if curr_node.left is not None:
            queue.append((curr_node.left, curr_node_depth + 1))
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_node_depth + 1))

    return max_depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Maximum Depth: " + str(maximum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Maximum Depth: " + str(maximum_depth(root)))


main()
