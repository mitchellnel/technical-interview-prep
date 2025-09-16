class Solution:
    def flipAndInvertImage(self, matrix):
        for row in matrix:
            left = 0
            right = len(row) - 1

            while left <= right:
                # flip
                row[left], row[right] = row[right], row[left]

                # invert
                row[left] ^= 1

                if left != right:
                    row[right] ^= 1

                left += 1
                right -= 1

        return matrix


if __name__ == "__main__":
    sol = Solution()

    assert sol.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]) == [
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]

    assert sol.flipAndInvertImage(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    ) == [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]

    print("All test cases passed.")
