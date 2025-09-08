from collections import deque


class Solution:
    def countClosedIslands(self, matrix):
        WATER_DEF = 0
        LAND_DEF = 1
        VISITED_DEF = -1

        N_ROWS = len(matrix)
        N_COLS = len(matrix[0])

        def bfs(start_row, start_col):
            queue = deque()
            queue.append((start_row, start_col))

            is_closed = True
            while queue:
                row, col = queue.popleft()

                for nr, nc in self.get_neighbors(N_ROWS, N_COLS, row, col):
                    if matrix[nr][nc] == LAND_DEF:
                        if nr == 0 or nr == N_ROWS - 1 or nc == 0 or nc == N_COLS - 1:
                            is_closed = False

                        matrix[nr][nc] = VISITED_DEF
                        queue.append((nr, nc))

            return is_closed

        n_closed_islands = 0
        for i in range(1, N_ROWS - 1):
            for j in range(1, N_COLS - 1):
                if matrix[i][j] == LAND_DEF:
                    matrix[i][j] = VISITED_DEF
                    if bfs(i, j):
                        n_closed_islands += 1

        return n_closed_islands

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

    assert (
        sol.countClosedIslands(
            [
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        == 1
    )

    assert (
        sol.countClosedIslands(
            [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        )
        == 2
    )

    print("All test cases passed.")
