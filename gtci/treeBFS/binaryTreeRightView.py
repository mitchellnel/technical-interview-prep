class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_right_view(root):
    right_view = []

    prev_node = root
    curr_traversal_depth = -1

    queue = [(root, 0)]

    while len(queue) > 0:
        curr_node, curr_node_depth = queue.pop(0)

        # check if the node we're looking at occurs at a new level
        if curr_node_depth != curr_traversal_depth:
            # append the previous node -- the rightmost node in the previous level
            right_view.append(prev_node)

            curr_traversal_depth = curr_node_depth

        if curr_node.left is not None:
            queue.append((curr_node.left, curr_traversal_depth + 1))
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_traversal_depth + 1))

        prev_node = curr_node

        if len(queue) == 0:
            right_view.append(prev_node)

    return right_view
