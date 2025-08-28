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
        # 3 scenarios:
        # - if p < root < q, return the LCA -> base case
        # - if p and q < root, traverse the left subtree
        # - if p and q > root, traverse the right subtree

        smaller = min(p.val, q.val)
        bigger = max(p.val, q.val)

        if smaller <= root.val and bigger >= root.val:
            return root
        elif root.val <= smaller:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > bigger:
            return self.lowestCommonAncestor(root.left, p, q)
