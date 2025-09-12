class Solution:
    def countRotations(self, arr):
        # rotation count == index of smallest element
        # smallest element is the only element whose previous is greater than itself
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if mid > left and arr[mid - 1] > arr[mid]:
                return mid

            if mid < right and arr[mid] > arr[mid + 1]:
                return mid + 1

            if arr[left] < arr[mid]:
                # min is either mid or to the right of mid
                left = mid + 1
            else:
                # min is either mid or to the left of mid
                right = mid - 1

        return 0


if __name__ == "__main__":
    sol = Solution()

    assert sol.countRotations([15, 18, 2, 3, 6, 12]) == 2
    assert sol.countRotations([7, 9, 11, 12, 5]) == 4
    assert sol.countRotations([7, 9, 11, 12, 15]) == 0
    assert sol.countRotations([1, 2, 3, 4, 5]) == 0

    print("All test cases passed.")
