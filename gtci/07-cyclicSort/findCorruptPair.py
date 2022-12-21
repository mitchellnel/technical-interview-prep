def find_corrupt_pair(nums):
    # cyclic sort
    curr_idx = 0
    while curr_idx < len(nums):
        correct_idx = nums[curr_idx] - 1
        if nums[curr_idx] != nums[correct_idx]:
            # swap
            nums[curr_idx], nums[correct_idx] = nums[correct_idx], nums[curr_idx]
        else:
            curr_idx += 1

    # iterate through the nums
    # when we find the mismatched pair
    #   - index + 1 is the missing number
    #   - number is the duplicate number
    for idx, num in enumerate(nums):
        if idx != num - 1:
            return [num, idx + 1]

    return [-1, -1]


def main():
    print(find_corrupt_pair([3, 1, 2, 5, 2]))
    print(find_corrupt_pair([3, 1, 2, 3, 6, 4]))


main()
