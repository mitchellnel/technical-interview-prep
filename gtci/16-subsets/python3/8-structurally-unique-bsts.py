class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findUniqueTrees(self, n):
        if n == 0:
            return []

        memo = {}

        def dfs(start, end):
            # base case -- no values remaining
            if start > end:
                return [None]

            # base case -- memoised
            if (start, end) in memo:
                return memo[(start, end)]

            trees = []

            # we fix one num to be the root
            # then the lower nums are the left subtree
            # and the greater nums are the right subtree
            for root_val in range(start, end + 1):
                left_subtrees = dfs(start, root_val - 1)
                right_subtrees = dfs(root_val + 1, end)

                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(root_val, left, right)

                        trees.append(root)

            memo[(start, end)] = trees
            return trees

        return dfs(1, n)


if __name__ == "__main__":
    sol = Solution()

    # n = 0 should return []
    assert sol.findUniqueTrees(0) == []

    # n = 1 should return 1 tree
    trees_1 = sol.findUniqueTrees(1)
    assert len(trees_1) == 1
    assert trees_1[0] is not None and trees_1[0].val == 1

    # Helper to serialize tree structure
    def serialize(root):
        if not root:
            return None
        return (root.val, serialize(root.left), serialize(root.right))

    # n = 2 should return 2 trees
    trees_2 = sol.findUniqueTrees(2)
    assert len(trees_2) == 2
    expected_2 = [
        (1, None, (2, None, None)),  # 1 as root, 2 as right child
        (2, (1, None, None), None),  # 2 as root, 1 as left child
    ]
    serialized_2 = [serialize(t) for t in trees_2]
    for e in expected_2:
        assert e in serialized_2

    # n = 3 should return 5 trees
    trees_3 = sol.findUniqueTrees(3)
    assert len(trees_3) == 5
    expected_3 = [
        (1, None, (2, None, (3, None, None))),
        (1, None, (3, (2, None, None), None)),
        (2, (1, None, None), (3, None, None)),
        (3, (1, None, (2, None, None)), None),
        (3, (2, (1, None, None), None), None),
    ]
    serialized_3 = [serialize(t) for t in trees_3]
    for e in expected_3:
        assert e in serialized_3
    trees_3 = sol.findUniqueTrees(3)
    assert len(trees_3) == 5

    print("All test cases passed.")
