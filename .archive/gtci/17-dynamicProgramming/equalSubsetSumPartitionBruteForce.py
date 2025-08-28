def can_partition(nums):
    s = sum(nums)

    # if s is odd, we can't have two subsets with equal sum
    if s % 2 != 0:
        return False

    return can_partition_recursive(nums, s / 2, 0)


def can_partition_recursive(nums, subset_sum, current_index):
    # base case
    if subset_sum == 0:
        return True

    n = len(nums)
    if n == 0 or current_index >= n:
        return False

    # recursive call after choosing the number at the current_index
    # if the number at the current index exceeds the sum, we shouldn't process this
    if nums[current_index] <= subset_sum:
        if can_partition_recursive(
            nums, subset_sum - nums[current_index], current_index + 1
        ):
            return True

    # recursive call after skipping the number at the current index
    return can_partition_recursive(nums, subset_sum, current_index + 1)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
