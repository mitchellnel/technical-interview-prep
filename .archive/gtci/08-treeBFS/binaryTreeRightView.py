from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_right_view(root):
    right_view = []

    queue = deque([root])
    while len(queue) > 0:
        level_size = len(queue)

        for i in range(level_size):
            curr_node = queue.popleft()

            if i == level_size - 1:
                right_view.append(curr_node)

            # add children to queue
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)

    return right_view


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = get_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val), end=" ")
    print()


main()
