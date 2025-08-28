def pairWithTargetSum(nums, target_sum):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target_sum:
            return [left, right]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

    return [-1, -1]


def pairWithHashTable(nums, target_sum):
    num_map = {}

    for idx, num in enumerate(nums):
        if target_sum - num in nums:
            return [idx, num_map[target_sum - num]]
        else:
            num_map[num] = idx

    return [-1, -1]


def main():
    print(pairWithTargetSum([1, 2, 3, 4, 6], 6))
    print(pairWithTargetSum([2, 5, 9, 11], 11))


main()
