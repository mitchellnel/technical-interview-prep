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


def find_cycle_start(nums, cycle_length):
    ptr1, ptr2 = nums[0], nums[0]

    # move ptr2 ahead cycle_length steps
    for _ in range(cycle_length):
        ptr2 = nums[ptr2]

    # increment both pointers until they meet at the cycle start
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1


def find_duplicate_number_two_pointers(nums):
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # find the cycle length
    current = nums[slow]
    cycle_length = 1
    while current != slow:
        current = nums[current]
        cycle_length += 1

    # find the start of the cycle
    return find_cycle_start(nums, cycle_length)


def main():
    print(find_duplicate_number([1, 4, 4, 3, 2]))
    print(find_duplicate_number([2, 1, 3, 3, 5, 4]))
    print(find_duplicate_number([2, 4, 1, 4, 4]))


main()
