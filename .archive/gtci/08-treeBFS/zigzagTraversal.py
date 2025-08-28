from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def zigzagTraversal(root):
    traversal = []

    right_to_left = False

    queue = deque([root])
    while len(queue) > 0:
        level_size = len(queue)
        curr_level_traversal = deque()

        for _ in range(level_size):
            curr_node = queue.popleft()

            # add the node to the current level based on traversal direction
            if not right_to_left:
                curr_level_traversal.append(curr_node.val)
            else:
                curr_level_traversal.appendleft(curr_node.val)

            # insert the children
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)

        traversal.append(list(curr_level_traversal))

        # reverse the traversal direction
        right_to_left = not right_to_left

    return traversal


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(zigzagTraversal(root)))


main()
