# O(n) time | O(1) space
def kadanesAlgorithm(array):
    max_ending_here = array[0]
    max_so_far = array[0]

    for i in range(1, len(array)):
        num = array[i]

        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far
