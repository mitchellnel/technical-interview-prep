class Solution:
    def searchNextLetter(self, letters, key):
        left = 0
        right = len(letters) - 1
        ceiling = 0

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] == key:
                return letters[mid + 1] if mid + 1 < len(letters) else letters[0]
            elif letters[mid] < key:
                left = mid + 1
            elif letters[mid] > key:
                ceiling = mid
                right = mid - 1

        return letters[ceiling]


if __name__ == "__main__":
    sol = Solution()

    assert sol.searchNextLetter(["a", "c", "f", "h"], "f") == "h"
    assert sol.searchNextLetter(["a", "c", "f", "h"], "b") == "c"
    assert sol.searchNextLetter(["a", "c", "f", "h"], "m") == "a"
    assert sol.searchNextLetter(["a", "c", "f", "h"], "h") == "a"

    print("All test cases passed.")
