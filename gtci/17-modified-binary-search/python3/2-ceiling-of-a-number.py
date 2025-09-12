class Solution:
    def searchCeilingOfANumber(self, arr, key):
        if not arr:
            return -1

        left = 0
        right = len(arr) - 1
        ceiling_idx = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                left = mid + 1
            elif arr[mid] > key:
                ceiling_idx = mid
                right = mid - 1

        return ceiling_idx


if __name__ == "__main__":
    sol = Solution()

    assert sol.searchCeilingOfANumber([4, 6, 10], 6) == 1
    assert sol.searchCeilingOfANumber([1, 3, 8, 10, 15], 12) == 4
    assert sol.searchCeilingOfANumber([4, 6, 10], 17) == -1
    assert sol.searchCeilingOfANumber([4, 6, 10], -1) == 0

    print("All test cases passed.")
