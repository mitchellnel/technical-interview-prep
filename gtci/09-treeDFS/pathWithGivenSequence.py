class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def path_with_given_sequence(tree, sequence):
    return path_with_given_sequence_helper(tree, sequence, 0)


def path_with_given_sequence_helper(tree, sequence, curr_seq_index):
    # DFS
    # base case
    if tree is None:
        return curr_seq_index == len(sequence)
    if tree.val != sequence[curr_seq_index]:
        return False

    # move onto next value in the sequence
    curr_seq_index += 1

    # explore rest of tree using DFS
    if path_with_given_sequence_helper(tree.left, sequence, curr_seq_index):
        return True
    if path_with_given_sequence_helper(tree.right, sequence, curr_seq_index):
        return True

    return False


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(path_with_given_sequence(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(path_with_given_sequence(root, [1, 1, 6])))


main()
