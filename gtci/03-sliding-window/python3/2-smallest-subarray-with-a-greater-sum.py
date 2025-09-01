import math


class Solution:
    def findMinSubArray(self, s, arr):
        min_subarray_size = math.inf

        window_start = 0
        window_sum = 0
        for window_end in range(len(arr)):
            window_sum += arr[window_end]

            # shrink the window as much as possible until window_sum < s
            while window_sum >= s:
                min_subarray_size = min(
                    min_subarray_size, window_end - window_start + 1
                )

                window_sum -= arr[window_start]
                window_start += 1

        return min_subarray_size if min_subarray_size != math.inf else 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.findMinSubArray(7, [2, 1, 5, 2, 3, 2]) == 2
    assert sol.findMinSubArray(7, [2, 1, 5, 2, 8]) == 1
    assert sol.findMinSubArray(8, [3, 4, 1, 1, 6]) == 3
    print("All test cases passed.")
