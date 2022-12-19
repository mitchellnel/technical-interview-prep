class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def count_paths_for_sum(tree, path_sum):
    return count_paths_for_sum_helper(tree, path_sum, 0)


def count_paths_for_sum_helper(tree, path_sum, path_length):
    # DFS
    # base cases
    if tree is None:
        return 0
    if (
        path_sum == tree.val
        and path_length != 0
        and tree.left is None
        and tree.right is None
    ):
        # leaf base case
        return 1

    new_path_sum = path_sum - tree.val

    path_count = 0
    if tree.left is not None:
        # there may be a path that ends here, but also a path that continues further along
        if path_sum == tree.val and path_length != 0:
            path_count += 1

        path_count += count_paths_for_sum_helper(tree.left, path_sum, 0)
        path_count += count_paths_for_sum_helper(
            tree.left, new_path_sum, path_length + 1
        )
    if tree.right is not None:
        if path_sum == tree.val and path_length != 0:
            path_count += 1

        path_count += count_paths_for_sum_helper(tree.right, path_sum, 0)
        path_count += count_paths_for_sum_helper(
            tree.right, new_path_sum, path_length + 1
        )

    return path_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree 1 has paths: " + str(count_paths_for_sum(root, 11)))

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    print("Tree 2 has paths: " + str(count_paths_for_sum(root, 12)))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(-7)
    root.right.left.right = TreeNode(7)
    print("Tree 3 has paths: " + str(count_paths_for_sum(root, 3)))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(-7)
    root.right.left.right = TreeNode(7)
    print("Tree 4 has paths: " + str(count_paths_for_sum(root, 4)))


main()
