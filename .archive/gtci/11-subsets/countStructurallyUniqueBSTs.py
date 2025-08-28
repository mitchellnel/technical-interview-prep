class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_unique_trees(n):
    if n <= 1:
        return 1

    count = 0

    for i in range(1, n + 1):
        # making i the root of the subtree
        left_subtrees_count = count_unique_trees(i - 1)
        right_subtrees_count = count_unique_trees(n - i)

        count += left_subtrees_count * right_subtrees_count

    return count


def count_unique_trees_dp(n):
    return count_unique_trees_dp_helper({}, n)


def count_unique_trees_dp_helper(dp, n):
    if n in dp:
        return dp[n]

    if n <= 1:
        return 1

    count = 0

    for i in range(1, n + 1):
        # making i the root of the subtree
        left_subtrees_count = count_unique_trees(i - 1)
        right_subtrees_count = count_unique_trees(n - i)

        count += left_subtrees_count * right_subtrees_count

    # memoise
    dp[n] = count

    return count


def main():
    print("Total trees: " + str(count_unique_trees(2)))
    print("Total trees: " + str(count_unique_trees(3)))


main()
