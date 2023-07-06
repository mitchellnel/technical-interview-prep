def quadrupletSumToTarget(nums, target):
    quadruplets = []

    nums.sort()

    for i in range(len(nums) - 3):
        # skip same element to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            # skip same element to avoid duplicates
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            searchPairs(nums, target, i, j, quadruplets)

    return quadruplets


def searchPairs(nums, target, first, second, quadruplets):
    left = second + 1
    right = len(nums) - 1

    while left < right:
        curr_sum = nums[first] + nums[second] + nums[left] + nums[right]

        if curr_sum == target:
            quadruplets.append([nums[first], nums[second], nums[left], nums[right]])

            left += 1
            right -= 1

            # skip same element to avoid duplicates
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
        elif curr_sum < target:
            # look for a bigger sum
            left += 1
        else:
            # look for a smaller sum
            right -= 1


def main():
    print(quadrupletSumToTarget([4, 1, 2, -1, 1, -3], 1))
    print(quadrupletSumToTarget([2, 0, -1, 1, -2, 2], 2))


main()
