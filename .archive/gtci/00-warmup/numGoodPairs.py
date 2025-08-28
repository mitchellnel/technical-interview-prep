def numGoodPairs(nums):
    num_freq = {}

    goodPairCount = 0
    for num in nums:
        if num not in num_freq:
            num_freq[num] = 0

        num_freq[num] += 1

        if num_freq[num] > 1:
            goodPairCount += num_freq[num] - 1

    return goodPairCount


def main():
    nums1 = [1, 2, 3, 1, 1, 3]
    result1 = numGoodPairs(nums1)
    print("Result 1:", result1, "(Expected: 4)")

    nums2 = [1, 1, 1, 1]
    result2 = numGoodPairs(nums2)
    print("Result 2:", result2, "(Expected: 6)")

    nums3 = [1, 2, 3]
    result3 = numGoodPairs(nums3)
    print("Result 3:", result3, "(Expected: 0)")


main()
