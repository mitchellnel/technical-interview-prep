class Solution:
    def findSubarrays(self, arr, target):
        if target < 1:
            return []

        result = []

        window_start = 0
        window_product = 1
        for window_end in range(len(arr)):
            window_product *= arr[window_end]

            while window_start < len(arr) and window_product >= target:
                window_product //= arr[window_start]

                window_start += 1

            subarray_slider = window_end
            while subarray_slider >= window_start:
                result.append(arr[subarray_slider : window_end + 1])
                subarray_slider -= 1

        return result


if __name__ == "__main__":
    sol = Solution()

    assert sol.findSubarrays([2, 5, 3, 10], 30) == [[2], [5], [2, 5], [3], [5, 3], [10]]
    assert sol.findSubarrays([8, 2, 6, 5], 50) == [
        [8],
        [2],
        [8, 2],
        [6],
        [2, 6],
        [5],
        [6, 5],
    ]

    print("All test cases passed.")
