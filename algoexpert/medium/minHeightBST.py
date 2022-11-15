# O(n) time | O(n) space
def minHeightBst(array):
    # array is sorted, so take the middle and use that as the root
    insertion_order = []

    middle = int(len(array) / 2)

    bst = BST(array[middle])

    insertion_order += minHeightBstHelper(array[:middle])
    insertion_order += minHeightBstHelper(array[middle + 1 :])

    for num in insertion_order:
        bst.insert(num)

    return bst


def minHeightBstHelper(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array

    insertion_order = []

    middle = int(len(array) / 2)
    insertion_order.append(array[middle])

    insertion_order += minHeightBstHelper(array[:middle])
    insertion_order += minHeightBstHelper(array[middle + 1 :])

    return insertion_order


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
