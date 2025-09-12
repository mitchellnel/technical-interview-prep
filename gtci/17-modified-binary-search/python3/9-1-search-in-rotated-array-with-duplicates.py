class Solution:
    def search(self, arr, key):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == key:
                return mid

            # duplicates, we don't know which side is sorted, so move left and right up by one
            if arr[left] == arr[mid] == arr[right]:
                left += 1
                right -= 1
                continue

            if arr[left] <= arr[mid]:  # left half is sorted
                if key >= arr[left] and key < arr[mid]:  # target in the left half
                    right = mid - 1
                else:
                    left = mid + 1  # target in the right half
            else:  # right half is sorted
                if key > arr[mid] and key <= arr[right]:
                    left = mid + 1  # target is in the right half
                else:
                    right = mid - 1  # target is in the left half

        return -1


if __name__ == "__main__":
    sol = Solution()

    assert sol.search([4, 5, 7, 9, 10, -1, 2], 10) == 4
    assert sol.search([4, 5, 7, 9, 10, -1, 2], -1) == 5
    assert sol.search([4, 5, 7, 9, 10, -1, 2], 6) == -1

    assert sol.search([3, 7, 3, 3, 3], 7) == 1
    assert sol.search([3, 3, 3, 3, 3], 7) == -1
    assert sol.search([3, 3, 3, 3, 3], 3) in [0, 1, 2, 3, 4]

    print("All test cases passed.")
