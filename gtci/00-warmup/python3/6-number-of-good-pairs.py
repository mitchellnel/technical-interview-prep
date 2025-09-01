def numGoodPairs(nums):
    pair_count = 0
    freq_map = {}

    for num in nums:
        if num not in freq_map:
            freq_map[num] = 0

        pair_count += freq_map[num]
        freq_map[num] += 1

    return pair_count


if __name__ == "__main__":
    assert numGoodPairs([1, 2, 3, 1, 1, 3]) == 4
    assert numGoodPairs([1, 1, 1, 1]) == 6
    assert numGoodPairs([1, 2, 3]) == 0
    print("All test cases passed.")
