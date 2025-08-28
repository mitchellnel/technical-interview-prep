from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_averages(root):
    if root is None:
        return []

    averages = []

    queue = deque([root])
    while len(queue) > 0:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            curr_node = queue.popleft()

            # add the node's value to the running sum
            level_sum += curr_node.val

            # add the node's children to the queue
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)

        # append the current level's average to our averages array
        averages.append(level_sum / level_size)

    return averages


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(level_averages(root)))


main()
