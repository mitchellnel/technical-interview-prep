class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_averages(root):
    averages = []

    curr_depth = 0

    queue = [(root, 0)]
    running_sum = 0
    n_elements_in_level = 0
    while len(queue) > 0:
        curr_node, curr_node_depth = queue.pop(0)

        # check if next node we're looking at occurs in new level
        if curr_node_depth != curr_depth:
            # add the average to our results list
            averages.append(running_sum / n_elements_in_level)

            # reset variables
            running_sum = 0
            n_elements_in_level = 0

            # update current depth
            curr_depth = curr_node_depth

        # append children to end of queue
        if curr_node.left is not None:
            queue.append((curr_node.left, curr_depth + 1))
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_depth + 1))

        # add to the running sum
        running_sum += curr_node.val
        n_elements_in_level += 1

    # add the average for the last level
    averages.append(running_sum / n_elements_in_level)

    return averages
