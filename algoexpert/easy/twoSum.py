# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    sub_values = {}

    for num in array:
        if targetSum - num not in sub_values.keys():
            sub_values[num] = targetSum - num
        else:
            return [num, targetSum - num]

    return []


# O(nlog(n)) time | O(1) space
def twoNumberSum_pointers(array, targetSum):
    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]

        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1

    return []
