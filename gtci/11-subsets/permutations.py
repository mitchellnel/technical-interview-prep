from collections import deque


def find_permutations(nums):
    result = []

    permutations = deque([[]])

    for num in nums:
        # take all existing permutations, and add the current number to create
        #   new permutations
        n = len(permutations)
        for _ in range(n):
            old_permutation = permutations.popleft()

            # create a new permutation by adding the current number at every
            #   position in the old permutation
            for i in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)

                new_permutation.insert(i, num)

                if len(new_permutation) == len(nums):
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)

    return result


# recursive
def generate_permutations(nums):
    result = []
    generate_permutations_helper(nums, 0, [], result)
    return result


def generate_permutations_helper(nums, idx, curr_permutation, result):
    if idx == len(nums):
        result.append(curr_permutation)
    else:
        # create a new permutation by adding the current number at every position
        for i in range(len(curr_permutation) + 1):
            new_permutation = list(curr_permutation)

            new_permutation.insert(i, nums[idx])

            generate_permutations_helper(nums, idx + 1, new_permutation, result)


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
