class Solution:
    def findRange(self, arr, key):
        if not arr:
            return [-1, -1]

        def find_first_occurrence():
            left = 0
            right = len(arr) - 1
            first = -1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == key:
                    first = mid
                    right = mid - 1
                elif arr[mid] < key:
                    left = mid + 1
                elif arr[mid] > key:
                    right = mid - 1

            return first

        def find_last_occurrence():
            left = 0
            right = len(arr) - 1
            last = -1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == key:
                    last = mid
                    left = mid + 1
                elif arr[mid] < key:
                    left = mid + 1
                elif arr[mid] > key:
                    right = mid - 1

            return last

        return [find_first_occurrence(), find_last_occurrence()]


if __name__ == "__main__":
    sol = Solution()

    assert sol.findRange([4, 6, 6, 6, 9], 6) == [1, 3]
    assert sol.findRange([1, 3, 8, 10, 15], 10) == [3, 3]
    assert sol.findRange([1, 3, 8, 10, 15], 12) == [-1, -1]

    print("All test cases passed.")
