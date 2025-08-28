class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def all_paths_for_sum(tree, path_sum):
    paths_for_sum = []

    all_path_for_sum_helper(tree, path_sum, [], paths_for_sum)

    return paths_for_sum


def all_path_for_sum_helper(tree, path_sum, current_path, paths_for_sum):
    # DFS
    # base case
    if tree is None:
        return
    if tree.left is None and tree.right is None:
        # leaf node
        if tree.val == path_sum:
            paths_for_sum.append(current_path + [tree.val])

    # not leaf node
    # get subtract this node's value from the sum
    new_path_sum = path_sum - tree.val

    # update the current path
    new_current_path = current_path + [tree.val]

    # find this new_path_sum in the node's children
    if tree.left is not None:
        all_path_for_sum_helper(
            tree.left, new_path_sum, new_current_path, paths_for_sum
        )
    if tree.right is not None:
        all_path_for_sum_helper(
            tree.right, new_path_sum, new_current_path, paths_for_sum
        )


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print(
        "Tree paths with required_sum "
        + str(required_sum)
        + ": "
        + str(all_paths_for_sum(root, required_sum))
    )


main()
