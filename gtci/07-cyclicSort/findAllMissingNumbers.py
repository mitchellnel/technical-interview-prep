def find_all_missing_numbers(nums):
    missing = []

    curr_idx = 0
    while curr_idx < len(nums):
        correct_idx = nums[curr_idx] - 1
        if correct_idx < len(nums) and nums[curr_idx] != nums[correct_idx]:
            nums[curr_idx], nums[correct_idx] = nums[correct_idx], nums[curr_idx]
        else:
            curr_idx += 1

    for idx, num in enumerate(nums):
        if idx != num - 1:
            missing.append(idx + 1)

    return missing


def main():
    print(find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_all_missing_numbers([2, 4, 1, 2]))
    print(find_all_missing_numbers([2, 3, 2, 1]))


main()
