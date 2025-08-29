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
    nums1 = [1, 2, 3, 1, 1, 3]
    print(numGoodPairs(nums1))  # Output: 4

    nums2 = [1, 1, 1, 1]
    print(numGoodPairs(nums2))  # Output: 6

    nums3 = [1, 2, 3]
    print(numGoodPairs(nums3))  # Output: 0
