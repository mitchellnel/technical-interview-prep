def tripletSumToZero(nums):
    triplets = []

    nums.sort()

    for i in range(len(nums)):
        # skip same element to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        searchPair(nums, -nums[i], i + 1, triplets)

    return triplets


def searchPair(nums, target_sum, left, triplets):
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target_sum:
            # found the triplet
            triplets.append([-target_sum, nums[left], nums[right]])

            left += 1
            right -= 1

            # skip the same element to avoid duplicate triplets
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif target_sum > current_sum:
            # we need a pair with a bigger sum
            left += 1
        else:
            # we need a pair with a smaller sum
            right -= 1


def main():
    print(tripletSumToZero([-3, 0, 1, 2, -1, 1, -2]))
    print(tripletSumToZero([-5, 2, -1, -2, 3]))


main()
