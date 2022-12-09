def can_partition(nums):
    s = sum(nums)

    # if s is odd, we can't have two subsets with equal sum
    if s % 2 != 0:
        return False

    dp = [[-1 for _ in range(int(s / 2) + 1)] for _ in range(len(nums))]

    return True if can_partition_recursive(dp, nums, int(s / 2), 0) == 1 else False


def can_partition_recursive(dp, nums, subset_sum, current_index):
    # base case
    if subset_sum == 0:
        return True

    n = len(nums)
    if n == 0 or current_index >= n:
        return False

    # if we have not already processed this problem before:
    if dp[current_index][subset_sum] == -1:
        # recursive call after choosing the number at the current_index
        # if the number at the current index exceeds the sum, we shouldn't process this
        if nums[current_index] <= subset_sum:
            if can_partition_recursive(
                dp, nums, subset_sum - nums[current_index], current_index + 1
            ):
                dp[current_index][subset_sum] = 1
                return 1

        # recursive call after skipping the number at the current index
        dp[current_index][subset_sum] = can_partition_recursive(
            dp, nums, subset_sum, current_index + 1
        )

    return dp[current_index][subset_sum]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
