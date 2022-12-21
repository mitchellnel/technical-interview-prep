def cyclic_sort(nums):
    curr_idx = 0
    while curr_idx < len(nums):
        correct_idx = nums[curr_idx] - 1

        if nums[curr_idx] != nums[correct_idx]:
            # swap
            nums[curr_idx], nums[correct_idx] = nums[correct_idx], nums[curr_idx]
        else:
            curr_idx += 1

    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
