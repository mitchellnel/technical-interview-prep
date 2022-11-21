class TreeInfo:
    def __init__(self, max_branch_sum, max_path_sum):
        self.max_branch_sum = max_branch_sum
        self.max_path_sum = max_path_sum


# O(n) time | O(log(n)) space
def maxPathSum(tree):
    return max_path_sum_helper(tree).max_path_sum


def max_path_sum_helper(tree):
    # base case
    # - no branch sum
    # - max path sum is the minimum
    if tree is None:
        return TreeInfo(0, float("-inf"))

    # recursive step
    left_subtree_info = max_path_sum_helper(tree.left)
    right_subtree_info = max_path_sum_helper(tree.right)

    # extra calculations
    max_child_branch_sum = max(
        left_subtree_info.max_branch_sum, right_subtree_info.max_branch_sum
    )

    value = tree.value

    # the max branch sum at out current node is either
    # - the root value itself (if max_child_branch_sum < 0)
    # - the expected max_child_branch_sum + value
    # value may itself be negative, but the branch must go through it
    #     (or it wouldn't be a branch), so we don't have the case of
    #     just max_child_branch_sum
    max_branch_sum = max(value, max_child_branch_sum + value)

    # the max path sum at out current node is one of:
    # - the max branch sum at the current node
    # - the "triangle" of the left subtree's max branch sum, the current
    #    node, and the right subtree's max branch sum
    # - the max path sum of the left subtree
    # - the max path sum of the right subtree
    # in the latter two cases, the root value may reduce the value of the
    #     path sum, so we skip it
    max_path_sum = max(
        max_branch_sum,
        left_subtree_info.max_branch_sum + right_subtree_info.max_branch_sum + value,
        left_subtree_info.max_path_sum,
        right_subtree_info.max_path_sum,
    )

    return TreeInfo(max_branch_sum, max_path_sum)
