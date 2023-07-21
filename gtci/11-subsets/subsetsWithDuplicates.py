def find_subsets_with_duplicates(nums):
    subsets = [[]]

    # sort to put all of the duplicates next to each other
    nums.sort()

    # use these variables to keep track of which subsets to use to create new
    #   subsets
    start_idx, end_idx = 0, 0

    for idx, num in enumerate(nums):
        start_idx = 0

        # if the current and the previous elements are the same, then crate new
        #   subsets only from the subsets added in the previous step
        if idx > 0 and nums[idx] == nums[idx - 1]:
            start_idx = end_idx + 1

        end_idx = len(subsets) - 1

        for j in range(start_idx, end_idx + 1):
            subset = subsets[j]

            new_subset = list(subset)
            new_subset.append(num)

            subsets.append(new_subset)

    return subsets


def main():
    print(
        "Here is the list of subsets: " + str(find_subsets_with_duplicates([1, 3, 3]))
    )
    print(
        "Here is the list of subsets: "
        + str(find_subsets_with_duplicates([1, 5, 3, 3]))
    )


main()
