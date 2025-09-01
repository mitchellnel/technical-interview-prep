class Solution:
    def findLength(self, arr, k):
        max_length = 0

        zero_count = 0
        window_start = 0
        for window_end in range(len(arr)):
            window_size = window_end - window_start + 1

            if arr[window_end] == 0:
                zero_count += 1

            if zero_count <= k:
                max_length = max(max_length, window_size)

            while zero_count > k:
                if arr[window_start] == 0:
                    zero_count -= 1

                window_start += 1
                window_size = window_end - window_start + 1

        return max_length


if __name__ == "__main__":
    sol = Solution()
    assert sol.findLength([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) == 6
    assert sol.findLength([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) == 9
    assert sol.findLength([1, 0, 0, 1, 1, 0, 1, 1], 2) == 6

    print("All test cases passed.")
