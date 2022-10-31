# O(n^2) time | O(n^2) space
def fourNumberSum(array, targetSum):
    quadruplets = []

    all_pair_sums = {}

    for i in range(1, len(array) - 1):
        # look in hashmap indexing with elements[i:j]
        for j in range(i + 1, len(array)):
            curr_sum = array[i] + array[j]

            diff = targetSum - curr_sum

            if diff in all_pair_sums:
                for pair in all_pair_sums[diff]:
                    quadruplets.append(pair + [array[i], array[j]])

        # build hashmap using elements [0:i]
        for k in range(0, i):
            curr_sum = array[i] + array[k]

            if curr_sum not in all_pair_sums:
                all_pair_sums[curr_sum] = [[array[k], array[i]]]
            else:
                all_pair_sums[curr_sum].append([array[k], array[i]])

    return quadruplets
