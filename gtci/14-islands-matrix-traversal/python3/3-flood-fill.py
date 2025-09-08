class Solution:
    def floodFill(self, matrix, x, y, newColor):
        N_ROWS = len(matrix)
        N_COLS = len(matrix[0])

        original_color = matrix[x][y]

        def dfs(start_row, start_col):
            stack = [(start_row, start_col)]

            while stack:
                row, col = stack.pop()

                for nr, nc in self.get_neighbors(N_ROWS, N_COLS, row, col):
                    if matrix[nr][nc] == original_color:
                        stack.append((nr, nc))
                        matrix[nr][nc] = newColor

        matrix[x][y] = newColor
        dfs(x, y)
        return matrix

    def get_neighbors(self, n_rows, n_cols, row, col):
        neighbours = []

        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in DIRECTIONS:
            nr = row + dr
            nc = col + dc

            if nr >= 0 and nr < n_rows and nc >= 0 and nc < n_cols:
                neighbours.append((nr, nc))

        return neighbours


if __name__ == "__main__":
    sol = Solution()

    assert sol.floodFill(
        [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1],
        ],
        1,
        1,
        2,
    ) == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]

    assert sol.floodFill(
        [
            [0, 0, 0],
            [0, 1, 1],
        ],
        1,
        1,
        5,
    ) == [
        [0, 0, 0],
        [0, 5, 5],
    ]

    print("All test cases passed.")
