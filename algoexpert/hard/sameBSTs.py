# O(n^2) time | O(n^2) space
def sameBSTs_n2(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    elif not arrayOne and not arrayTwo:
        return True
    elif arrayOne[0] != arrayTwo[0]:
        return False

    root_one = arrayOne[0]
    root_two = arrayTwo[0]

    left_sub_one = []
    left_sub_two = []
    right_sub_one = []
    right_sub_two = []
    for i in range(1, len(arrayOne)):
        if arrayOne[i] < root_one:
            left_sub_one.append(arrayOne[i])
        else:
            right_sub_one.append(arrayOne[i])

        if arrayTwo[i] < root_two:
            left_sub_two.append(arrayTwo[i])
        else:
            right_sub_two.append(arrayTwo[i])

    return sameBSTs_n2(left_sub_one, left_sub_two) and sameBSTs_n2(
        right_sub_one, right_sub_two
    )


# O(n^2) time | O(d) space
def sameBsts(arrayOne, arrayTwo):
    return sameBSTsHelper(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def sameBSTsHelper(arrayOne, arrayTwo, root_idx_one, root_idx_two, min_val, max_val):
    # only do this is we can't find anything smaller - end of our recursion
    if root_idx_one == -1 or root_idx_two == -1:
        return root_idx_one == root_idx_two

    # base case - roots of subtrees must be the same
    if arrayOne[root_idx_one] != arrayTwo[root_idx_two]:
        return False

    left_root_idx_one = getIdxOfFirstSmaller(arrayOne, root_idx_one, min_val)
    left_root_idx_two = getIdxOfFirstSmaller(arrayTwo, root_idx_two, min_val)
    right_root_idx_one = getIdxOfFirstLarger(arrayOne, root_idx_one, max_val)
    right_root_idx_two = getIdxOfFirstLarger(arrayTwo, root_idx_two, max_val)

    current_val = arrayOne[root_idx_one]

    left_same = sameBSTsHelper(
        arrayOne, arrayTwo, left_root_idx_one, left_root_idx_two, min_val, current_val
    )
    right_same = sameBSTsHelper(
        arrayOne, arrayTwo, right_root_idx_one, right_root_idx_two, current_val, max_val
    )

    return left_same and right_same


def getIdxOfFirstSmaller(array, start, min_val):
    # find the index of the first smaller value after the starting index
    # make sure that this value is greater than or equal to the min_val,
    #     which is the value of the previous parent node in the BST
    # if it isn't, then that value is located in the left subtree of the
    #     previous parent node
    for i in range(start + 1, len(array)):
        if array[i] < array[start] and array[i] >= min_val:
            return i
    # we've run out of values to look at
    return -1


def getIdxOfFirstLarger(array, start, max_val):
    # find the index of the first larger/equal value after the starting index
    # make sure that this value is less than the max_val, which is the
    #     value of the previous parent node in the BSt
    # if it isn't, then that value is located in the right subtree of
    #     previous parent node
    for i in range(start + 1, len(array)):
        if array[i] >= array[start] and array[i] < max_val:
            return i
    # we've run out of values to look at
    return -1
