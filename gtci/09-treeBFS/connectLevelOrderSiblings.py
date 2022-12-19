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
