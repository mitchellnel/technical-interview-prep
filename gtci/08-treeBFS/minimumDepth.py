class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def minimum_depth(root):
    queue = [(root, 0)]

    while len(queue) > 0:
        curr_node, curr_node_depth = queue.pop(0)

        # when we run into our first leaf node, its depth is the min depth
        if curr_node.left is None and curr_node.right is None:
            return curr_node_depth

        # append children to end of queue
        if curr_node.left is not None:
            queue.append((curr_node.left, curr_node_depth + 1))
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_node_depth + 1))
