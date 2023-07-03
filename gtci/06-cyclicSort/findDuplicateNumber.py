def find_duplicate_number(nums):
    curr_idx = 0
    while curr_idx < len(nums):
        # if in the wrong place
        correct_idx = nums[curr_idx] - 1
        if curr_idx != correct_idx:
            if correct_idx < len(nums) and nums[curr_idx] != nums[correct_idx]:
                # swap
                nums[curr_idx], nums[correct_idx] = nums[correct_idx], nums[curr_idx]
            else:
                # we've found the duplicate
                return nums[curr_idx]
        else:
            curr_idx += 1

    return -1


def main():
    print(find_duplicate_number([1, 4, 4, 3, 2]))
    print(find_duplicate_number([2, 1, 3, 3, 5, 4]))
    print(find_duplicate_number([2, 4, 1, 4, 4]))


main()
