class Solution:
    def findMaxSumSubArray(self, K, arr):
        max_sum = float("-inf")

        window_start = 0
        window_sum = 0

        for window_end in range(len(arr)):
            window_sum += arr[window_end]

            if window_end >= K - 1:
                max_sum = max(max_sum, window_sum)

                window_sum -= arr[window_start]
                window_start += 1

        return max_sum


if __name__ == "__main__":
    sol = Solution()

    assert sol.findMaxSumSubArray(3, [2, 1, 5, 1, 3, 2]) == 9
    assert sol.findMaxSumSubArray(2, [2, 3, 4, 1, 5]) == 7

    print("All test cases passed.")
