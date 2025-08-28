def find_smallest_missing_positive_number(nums):
    # cyclic sort
    curr_idx = 0
    while curr_idx < len(nums):
        correct_idx = nums[curr_idx] - 1
        # if correct_idx is out of range, leave it be
        if (
            correct_idx >= 0
            and correct_idx < len(nums)
            and nums[curr_idx] != nums[correct_idx]
        ):
            # swap
            nums[curr_idx], nums[correct_idx] = nums[correct_idx], nums[curr_idx]
        else:
            curr_idx += 1

    # iterate through nums
    # first mismatch is our missing number (it will be idx + 1)
    for idx, num in enumerate(nums):
        if idx != num - 1:
            return idx + 1

    return len(nums) + 1


def main():
    print(find_smallest_missing_positive_number([-3, 1, 5, 4, 2]))
    print(find_smallest_missing_positive_number([3, -2, 0, 1, 2]))
    print(find_smallest_missing_positive_number([3, 2, 5, 1]))
    print(find_smallest_missing_positive_number([33, 37, 5]))
    print(find_smallest_missing_positive_number([-1, -2, -3]))


main()
