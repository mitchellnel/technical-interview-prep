class Solution:
    def countIslands(self, matrix):
        WATER_DEF = 0
        ISLAND_DEF = 1

        N_ROWS = len(matrix)
        N_COLS = len(matrix[0])

        def dfs(row, col):
            stack = [(row, col)]

            while stack:
                [row, col] = stack.pop()

                # mark the cell as a water cell to indicate visited
                matrix[row][col] = WATER_DEF

                if row - 1 >= 0 and matrix[row - 1][col] == ISLAND_DEF:
                    stack.append((row - 1, col))

                if row + 1 < N_ROWS and matrix[row + 1][col] == ISLAND_DEF:
                    stack.append((row + 1, col))

                if col - 1 >= 0 and matrix[row][col - 1] == ISLAND_DEF:
                    stack.append((row, col - 1))

                if col + 1 < N_COLS and matrix[row][col + 1] == ISLAND_DEF:
                    stack.append((row, col + 1))

        totalIslands = 0
        for i in range(N_ROWS):
            for j in range(N_COLS):
                if matrix[i][j] == ISLAND_DEF:
                    totalIslands += 1
                    dfs(i, j)

        return totalIslands


if __name__ == "__main__":
    sol = Solution()

    assert (
        sol.countIslands(
            [
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
            ]
        )
        == 3
    )

    assert (
        sol.countIslands(
            [
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        == 1
    )

    print("All test cases passed.")
