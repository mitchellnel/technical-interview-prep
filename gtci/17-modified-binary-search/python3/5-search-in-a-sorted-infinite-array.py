import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


class Solution:
    def searchInfiniteSortedArray(self, reader, key):
        left = 0
        right = 1

        # find a finite window to perform the search in
        while reader.get(right) < key:
            left = right
            right *= 2  # double the window size on each step

        # perform the search
        while left <= right:
            mid = (left + right) // 2

            if reader.get(mid) == key:
                return mid
            elif reader.get(mid) < key:
                left = mid + 1
            elif reader.get(mid) > key:
                right = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    reader1 = ArrayReader([4, 6, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    assert sol.searchInfiniteSortedArray(reader1, 16) == 5
    assert sol.searchInfiniteSortedArray(reader1, 11) == -1

    reader2 = ArrayReader([1, 3, 8, 10, 15])
    assert sol.searchInfiniteSortedArray(reader2, 15) == 4
    assert sol.searchInfiniteSortedArray(reader2, 200) == -1

    print("All test cases passed.")
