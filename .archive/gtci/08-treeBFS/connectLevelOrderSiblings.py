from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end="")
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    if root is None:
        return None

    queue = deque([root])
    while len(queue) > 0:
        level_size = len(queue)

        prev = None
        for _ in range(level_size):
            curr = queue.popleft()

            # connect previous node to next node on level
            if prev is not None:
                prev.next = curr

            prev = curr

            # add children of curr node to queue
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

    return root


def connect_level_order_siblings_complex(root):
    queue = [(root, 0)]

    while len(queue) > 0:
        curr_node, curr_node_depth = queue.pop(0)

        # append children to end of queue
        if curr_node.left is not None:
            queue.append((curr_node.left, curr_node_depth + 1))
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_node_depth + 1))

        # look at the front node's depth in the queue
        next_node_tuple = queue[0] if len(queue) > 0 else None
        if next_node_tuple is not None:
            next_node, next_node_depth = next_node_tuple
            if next_node_depth == curr_node_depth:
                curr_node.next = next_node
            else:
                curr_node.next = None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
