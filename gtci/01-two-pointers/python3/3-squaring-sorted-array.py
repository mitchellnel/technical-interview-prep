class Solution:
    def makeSquares(self, arr):
        n = len(arr)
        squares = [0 for x in range(n)]

        squares_ptr = n - 1

        left = 0
        right = n - 1

        while left <= right:
            if abs(arr[left]) > abs(arr[right]):
                squares[squares_ptr] = arr[left] ** 2
                squares_ptr -= 1
                left += 1
            elif abs(arr[right]) >= abs(arr[left]):
                squares[squares_ptr] = arr[right] ** 2
                squares_ptr -= 1
                right -= 1

        return squares


if __name__ == "__main__":
    sol = Solution()
    arr = [-2, -1, 0, 1, 2]
    result = sol.makeSquares(arr)
    assert result == [0, 1, 1, 4, 4]

    arr2 = [-3, -2, -1, 0, 1, 2, 3, 3]
    result2 = sol.makeSquares(arr2)
    assert result2 == [0, 1, 1, 4, 4, 9, 9, 9]

    arr3 = [-3, -2, -1]
    result3 = sol.makeSquares(arr3)
    assert result3 == [1, 4, 9]
    print("All test cases passed.")
