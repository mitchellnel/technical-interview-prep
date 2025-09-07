class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findPaths(self, root, required_sum):
        results = []

        self.findPaths_helper(results, root, required_sum)

        return results

    def findPaths_helper(self, results, root, required_sum, path=[]):
        if root is None:
            return

        path.append(root.val)

        if root.left is None and root.right is None and root.val == required_sum:
            results.append(list(path))
        else:
            self.findPaths_helper(results, root.left, required_sum - root.val, path)
            self.findPaths_helper(results, root.right, required_sum - root.val, path)

        path.pop()  # backtrack


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(-3)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(3)

    assert sol.findPaths(root, 23) == [[12, 1, 10]]
    assert sol.findPaths(root, 16) == [[12, 7, -3], [12, 1, 3]]

    print("All test cases passed.")
