# O(n^2) time | O(n) space
def rightSmallerThan_naive(array):
    smaller_than = [0 for _ in range(len(array))]

    for i in range(len(array)):
        curr = array[i]
        for j in range(i, len(array)):
            if array[j] < curr:
                smaller_than[i] += 1

    return smaller_than


class RSTBST:
    # we use a custom BST class that at each node, stores the
    #     size of it's left subtree, i.e. all values less than
    #     it
    def __init__(self, value, left, right, left_subtree_size):
        self.value = value
        self.left = left
        self.right = right
        self.left_subtree_size = left_subtree_size

    def insert(self, value, right_smaller_count):
        if value < self.value:
            # we're going to add a value to the left subtree, so
            #     increment the size
            self.left_subtree_size += 1

            if self.left is not None:
                return self.left.insert(value, right_smaller_count)
            else:
                self.left = RSTBST(value, None, None, 0)
                return right_smaller_count
        else:
            # all of the values in the left subtree of self are
            #     strictly smaller than the value we're inserting
            right_smaller_count += self.left_subtree_size

            # only add an additional 1 if self is smaller than value
            if value > self.value:
                right_smaller_count += 1

            if self.right is not None:
                return self.right.insert(value, right_smaller_count)
            else:
                self.right = RSTBST(value, None, None, 0)
                return right_smaller_count


def rightSmallerThan(array):
    if len(array) == 0:
        return []

    right_smaller_counts = [0]

    last_idx = len(array) - 1
    root = RSTBST(array[last_idx], None, None, 0)

    for i in reversed(range(len(array) - 1)):
        right_smaller_counts.append(root.insert(array[i], 0))

    right_smaller_counts.reverse()

    return right_smaller_counts
