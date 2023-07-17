def find_first_k_missing_positive_numbers(nums, k):
    missing = []

    # cyclic sort
    curr_idx = 0
    while curr_idx < len(nums):
        correct_idx = nums[curr_idx] - 1
        if (
            correct_idx >= 0
            and correct_idx < len(nums)
            and nums[curr_idx] != nums[correct_idx]
        ):
            # swap
            nums[curr_idx], nums[correct_idx] = nums[correct_idx], nums[curr_idx]
        else:
            curr_idx += 1

    # use a hashmap to check if a number out of range appears in the array due to O(1)
    #   lookup time
    appears = {}

    # look for missing numbers
    for idx, num in enumerate(nums):
        appears[num] = True

        # make sure to only find first k
        if len(missing) < k and idx != num - 1:
            missing.append(idx + 1)

    # check we've found k missing numbers
    candidate_number = (
        len(nums) + 1
    )  # other missing nums will be those beyond our positive range
    while len(missing) < k:
        # check that our candidate does not exist in nums
        if candidate_number not in appears:
            missing.append(candidate_number)
        candidate_number += 1

    return missing


def main():
    print(find_first_k_missing_positive_numbers([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive_numbers([2, 3, 4], 3))
    print(find_first_k_missing_positive_numbers([-2, -3, 4], 2))


main()
