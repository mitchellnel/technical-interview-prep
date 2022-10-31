# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    one_ptr = 0
    two_ptr = 0

    min_diff = None
    min_diff_nums = []

    while one_ptr < len(arrayOne) and two_ptr < len(arrayTwo):
        diff = abs(arrayOne[one_ptr] - arrayTwo[two_ptr])

        if min_diff is None or diff < min_diff:
            min_diff = diff
            min_diff_nums = [arrayOne[one_ptr], arrayTwo[two_ptr]]

        if diff == 0:
            return [arrayOne[one_ptr], arrayTwo[two_ptr]]
        elif arrayOne[one_ptr] < arrayTwo[two_ptr]:
            one_ptr += 1
        elif arrayOne[one_ptr] > arrayTwo[two_ptr]:
            two_ptr += 1

    return min_diff_nums
