# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    triplets = []

    array.sort()

    for idx, num in enumerate(array):
        left = idx + 1
        right = len(array) - 1

        while left < right:
            curr_sum = num + array[left] + array[right]

            if curr_sum < targetSum:
                left += 1
            elif curr_sum > targetSum:
                right -= 1
            elif curr_sum == targetSum:
                triplets.append([num, array[left], array[right]])
                left += 1

    return triplets
