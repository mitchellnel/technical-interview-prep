class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order_successor(root, node):
    found_given_node = False

    queue = [(root, 0)]

    while len(queue) > 0:
        curr_node, curr_node_depth = queue.pop(0)

        # if we've previously found the given node, return this current node as the successor
        if found_given_node:
            return curr_node

        # when we run the given node, the next node in the queue is the successor
        if curr_node.val == node:
            found_given_node = True

        # append children to end of queue
        if curr_node.left is not None:
            queue.append((curr_node.left, curr_node_depth + 1))
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_node_depth + 1))
