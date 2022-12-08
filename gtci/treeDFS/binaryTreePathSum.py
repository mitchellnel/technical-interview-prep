class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def has_path_sum(tree, path_sum):
    # DFS
    # base case
    if tree is None:
        return False
    if tree.left is None and tree.right is None:
        # leaf node
        return tree.val == path_sum

    # not leaf node
    # get subtract this node's value from the sum
    new_path_sum = path_sum - tree.val

    # find this new_path_sum in the node's children
    if tree.left is not None and has_path_sum(tree.left, new_path_sum):
        return True
    if tree.right is not None and has_path_sum(tree.right, new_path_sum):
        return True

    return False


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path_sum(root, 23)))
    print("Tree has path: " + str(has_path_sum(root, 16)))


main()
