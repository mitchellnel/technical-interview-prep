class Solution:
    def search(self, arr, key):
        if not arr:
            return -1

        is_ascending = arr[0] <= arr[1]

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == key:
                return mid
            elif (is_ascending and arr[mid] < key) or (
                not is_ascending and arr[mid] > key
            ):
                left = mid + 1
            elif (is_ascending and arr[mid] > key) or (
                not is_ascending and arr[mid] < key
            ):
                right = mid - 1

        return -1  # element not found


if __name__ == "__main__":
    sol = Solution()

    assert sol.search([4, 6, 10], 10) == 2
    assert sol.search([1, 2, 3, 4, 5, 6, 7], 5) == 4
    assert sol.search([10, 6, 4], 10) == 0
    assert sol.search([7, 6, 5, 4, 3, 2, 1], 5) == 2
    assert sol.search([1, 3, 8, 3, 1], 3) in [1, 3]
    assert sol.search([3, 3, 3, 3, 3], 3) in [0, 1, 2, 3, 4]
    assert sol.search([], 5) == -1

    print("All test cases passed.")
