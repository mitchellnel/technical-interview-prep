from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # start by DFSing to p and q, keeping track of parents of each node on the way
        parent = {root: None}

        stack = [root]
        while p not in parent or q not in parent:
            curr_node = stack.pop()

            if curr_node.left is not None:
                stack.append(curr_node.left)
                parent[curr_node.left] = curr_node
            if curr_node.right is not None:
                stack.append(curr_node.right)
                parent[curr_node.right] = curr_node

        # find all the ancestors of p
        ancestors = set()

        curr_node = p
        while curr_node is not None:
            ancestors.add(curr_node)
            curr_node = parent[curr_node]

        # find lowest ancestor of q that is in ancestors of p
        curr_node = q
        while curr_node is not None and curr_node not in ancestors:
            curr_node = parent[curr_node]

        return curr_node
