class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def sum_of_path_numbers(tree):
    path_numbers = []

    get_path_numbers(tree, "", path_numbers)

    return sum([int(path_num) for path_num in path_numbers])


def get_path_numbers(tree, current_path, path_numbers):
    # DFS
    # base case
    if tree is None:
        return
    if tree.left is None and tree.right is None:
        # leaf node means end of path
        path_numbers.append(current_path + str(tree.val))

    # else not leaf node
    new_current_path = current_path + str(tree.val)

    if tree.left is not None:
        get_path_numbers(tree.left, new_current_path, path_numbers)
    if tree.right is not None:
        get_path_numbers(tree.right, new_current_path, path_numbers)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(sum_of_path_numbers(root)))


main()
