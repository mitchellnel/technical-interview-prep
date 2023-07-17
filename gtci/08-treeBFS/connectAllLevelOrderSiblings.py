from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end="")
        current = self
        while current:
            print(str(current.val) + " ", end="")
            current = current.next
        print()


def connect_all_level_order_siblings(root):
    if root is None:
        return None

    prev, curr = None, None
    queue = deque([root])
    while len(queue) > 0:
        curr = queue.popleft()

        # connect previous node to next node
        if prev is not None:
            prev.next = curr

        prev = curr

        # add children of curr node to queue
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

    return root


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_level_order_siblings(root)
    root.print_tree()


main()
