def tripletSumCloseToTarget(nums, target_sum):
    min_diff = float("inf")

    nums.sort()

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            target_diff = target_sum - nums[i] - nums[left] - nums[right]

            if target_diff == 0:
                # we've found a triplet with an exact sum
                return target_sum

            # the second part of the following if statement is to choose the
            #   smallest sum when have more than one solution
            if abs(target_diff) < abs(min_diff) or (
                abs(target_diff) == abs(min_diff) and target_diff > min_diff
            ):
                # save the closest and biggest difference
                min_diff = target_diff

            if target_diff > 0:
                # we need a triplet with a bigger sum
                left += 1
            else:
                # we need a triplet with a smaller sum
                right -= 1

    return target_sum - min_diff


def main():
    print(tripletSumCloseToTarget([-1, 0, 2, 3], 2))
    print(tripletSumCloseToTarget([-3, -1, 1, 2], 1))
    print(tripletSumCloseToTarget([1, 0, 1, 1], 100))
    print(tripletSumCloseToTarget([0, 0, 1, 1, 2, 6], 5))


main()
