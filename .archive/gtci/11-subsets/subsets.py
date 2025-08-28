def find_subsets(nums):
    # start with the empty subset
    subsets = [[]]

    for num in nums:
        # take all current subsets and add num to them to create a new subset

        # have to use n so the for loop will run to completion
        n = len(subsets)
        for i in range(n):
            subset = subsets[i]

            # create a brand new list (not another reference)
            new_subset = list(subset)
            new_subset.append(num)

            subsets.append(new_subset)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
