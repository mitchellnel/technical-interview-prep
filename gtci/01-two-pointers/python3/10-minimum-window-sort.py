import math


class Solution:
    def sort(self, arr):
        left = 1
        right = len(arr) - 2

        while left < len(arr):
            if arr[left] < arr[left - 1]:
                left -= 1
                break

            left += 1

        if left == len(arr):
            return 0  # already sorted

        while right >= 0:
            if arr[right] > arr[right + 1]:
                right += 1
                break
            right -= 1

        subarray_min = arr[left]
        subarray_max = arr[left]
        i = left
        while i <= right:
            subarray_min = min(subarray_min, arr[i])
            subarray_max = max(subarray_max, arr[i])

            i += 1

        while left > 0 and arr[left - 1] > subarray_min:
            left -= 1

        while right < len(arr) - 1 and arr[right + 1] < subarray_max:
            right += 1

        return right - left + 1


if __name__ == "__main__":
    sol = Solution()
    assert sol.sort([1, 2, 5, 3, 7, 10, 9, 12]) == 5
    assert sol.sort([1, 3, 2, 0, -1, 7, 10]) == 5
    assert sol.sort([1, 2, 3]) == 0
    assert sol.sort([3, 2, 1]) == 3
    assert sol.sort([3, 3, 2, 2]) == 4
    print("All test cases passed.")
