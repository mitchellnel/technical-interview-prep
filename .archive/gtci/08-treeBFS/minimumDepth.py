from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def minimum_depth(root):
    if root is None:
        return 0

    queue = deque([(root, 1)])

    while len(queue) > 0:
        curr_node, curr_node_depth = queue.popleft()

        # when we run into our first leaf node, its depth is the min depth
        if curr_node.left is None and curr_node.right is None:
            return curr_node_depth

        # append children to end of queue
        if curr_node.left is not None:
            queue.append((curr_node.left, curr_node_depth + 1))
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_node_depth + 1))

    return -1


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(minimum_depth(root)))


main()
