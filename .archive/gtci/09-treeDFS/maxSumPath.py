class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class MaxSumPath:
    def __init__(self):
        self.max_sum = float("-inf")

    def get_max_sum_path(self, root):
        self._calculate_max_sum_path(root)
        return self.max_sum

    def _calculate_max_sum_path(self, tree):
        # DFS
        # base case
        if tree is None:
            return 0

        # recursive step

        # ignore paths with negative sums
        left_max_sum = max(self._calculate_max_sum_path(tree.left), 0)
        right_max_sum = max(self._calculate_max_sum_path(tree.right), 0)

        local_max_sum = left_max_sum + right_max_sum + tree.val

        self.max_sum = max(self.max_sum, local_max_sum)

        return max(left_max_sum, right_max_sum) + tree.val


def main():
    maxPathSum = MaxSumPath()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(maxPathSum.get_max_sum_path(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(maxPathSum.get_max_sum_path(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(maxPathSum.get_max_sum_path(root)))


main()
