def find_missing_number(nums):
    curr_idx = 0
    while curr_idx < len(nums):
        correct_idx = nums[curr_idx]
        if nums[curr_idx] < len(nums) and nums[curr_idx] != nums[correct_idx]:
            # swap
            nums[curr_idx], nums[correct_idx] = nums[correct_idx], nums[curr_idx]
        else:
            curr_idx += 1

    # find the first number where the index does not match, the index is then our missing number
    for idx, num in enumerate(nums):
        if idx != num:
            return idx

    return len(nums)


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
