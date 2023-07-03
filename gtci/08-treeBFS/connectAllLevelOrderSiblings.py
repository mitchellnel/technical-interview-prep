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
    queue = [root]

    while len(queue) > 0:
        curr_node = queue.pop(0)

        # append children to end of queue
        if curr_node.left is not None:
            queue.append(curr_node.left)
        if curr_node.right is not None:
            queue.append(curr_node.right)

        # look at the front node's depth in the queue
        if len(queue) != 0:
            print(f"Connecting {curr_node.val} to {queue[0].val}")
            curr_node.next = queue[0]
        else:
            curr_node.next = None
