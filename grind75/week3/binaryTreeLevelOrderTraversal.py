# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []

        curr_depth = -1

        queue = [(root, 0)]
        while len(queue) > 0:
            curr_node, curr_node_depth = queue.pop(0)

            if curr_node is None:
                continue

            # check if node we're looking at occurs at a new depth
            if curr_node_depth != curr_depth:
                # add new list for this level
                traversal.append([])

                # move to a new depth
                curr_depth += 1

            # append children to end of queue
            if curr_node.left is not None:
                queue.append((curr_node.left, curr_node_depth + 1))
            if curr_node.right is not None:
                queue.append((curr_node.right, curr_node_depth + 1))

            # add value to the level whose list we're currently traversing
            traversal[-1].append(curr_node.val)

        return traversal
