class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def zigzagTraversal(root):
    traversal = []

    curr_depth = -1

    queue = [(root, 0)]
    while len(queue) > 0:
        curr_node, curr_node_depth = queue.pop(0)

        # check if next node we're looking at occurs in new level
        if curr_node_depth != curr_depth:
            # add new list for this level
            traversal.append([])

            # change the curr level we're looking at
            curr_depth = curr_node_depth

        # append children to end of queue
        if curr_node.left is not None:
            queue.append((curr_node.left, curr_depth + 1))
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_depth + 1))

        # add value to the level whose list we're currently traversing
        if curr_depth % 2 == 0:
            # if curr_depth is even, we traverse from left to right on the level, so simply append
            traversal[-1].append(curr_node.val)
        else:
            # else, we traverse from right to left on the level, so add to the front of the list
            traversal[-1].insert(0, curr_node.val)

    return traversal
