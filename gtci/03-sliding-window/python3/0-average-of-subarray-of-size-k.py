class Solution:
    def find_averages(self, K, arr):
        averages = []

        window_start = 0
        window_sum = 0
        for window_end in range(len(arr)):
            window_sum += arr[window_end]

            if window_end >= K - 1:
                averages.append(window_sum / 5)

                window_sum -= arr[window_start]
                window_start += 1

        return averages


if __name__ == "__main__":
    sol = Solution()
    result = sol.find_averages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    assert result == [2.2, 2.8, 2.4, 3.6, 2.8]

    print("All test cases passed.")
