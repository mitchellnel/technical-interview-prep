class Solution:
    def searchMinDiffElement(self, arr, key):
        if not arr:
            return -1

        left = 0
        right = len(arr) - 1

        min_difference_elem = None

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == key:
                return key
            elif arr[mid] < key:
                left = mid + 1
            elif arr[mid] > key:
                right = mid - 1

        # after the search:
        # - left is the largest element less than key
        # - right is the smallest element greater than key
        if left >= len(arr):
            return arr[right]

        if right < 0:
            return arr[left]

        if abs(arr[left] - key) < abs(arr[right] - key):
            return arr[left]
        else:
            return arr[right]


if __name__ == "__main__":
    sol = Solution()

    assert sol.searchMinDiffElement([4, 6, 10], 7) == 6
    assert sol.searchMinDiffElement([4, 6, 10], 4) == 4
    assert sol.searchMinDiffElement([1, 3, 8, 10, 15], 12) == 10
    assert sol.searchMinDiffElement([4, 6, 10], 17) == 10
    assert sol.searchMinDiffElement([4, 6, 10], -1) == 4
    assert sol.searchMinDiffElement([], 7) == -1

    print("All test cases passed.")
