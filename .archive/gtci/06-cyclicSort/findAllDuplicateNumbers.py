def find_all_duplicate_numbers(nums):
    duplicates = []

    curr_idx = 0
    while curr_idx < len(nums):
        correct_idx = nums[curr_idx] - 1
        if nums[curr_idx] != nums[correct_idx]:
            # swap
            nums[curr_idx], nums[correct_idx] = nums[correct_idx], nums[curr_idx]
        else:
            curr_idx += 1

    for idx, num in enumerate(nums):
        if idx != num - 1:
            duplicates.append(num)

    return duplicates


def main():
    print(find_all_duplicate_numbers([3, 4, 4, 5, 5]))
    print(find_all_duplicate_numbers([5, 4, 7, 2, 3, 5, 3]))


main()
