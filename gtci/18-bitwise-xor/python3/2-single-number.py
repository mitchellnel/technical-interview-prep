class Solution:
    def findSingleNumber(self, arr):
        num = arr[0]

        for i in range(1, len(arr)):
            num ^= arr[i]

        return num


if __name__ == "__main__":
    sol = Solution()

    assert sol.findSingleNumber([2, 2, 1]) == 1

    assert sol.findSingleNumber([4, 1, 2, 1, 2]) == 4

    assert sol.findSingleNumber([1]) == 1

    print("All test cases passed.")
