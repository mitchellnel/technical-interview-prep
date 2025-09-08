from collections import deque


class Solution:
    def maxAreaOfIsland(self, matrix):
        WATER_DEF = 0
        LAND_DEF = 1

        N_ROWS = len(matrix)
        N_COLS = len(matrix[0])

        def bfs(start_row, start_col):
            queue = deque()
            queue.append((start_row, start_col))

            island_area = 0
            while queue:
                row, col = queue.popleft()

                island_area += 1

                for nr, nc in self.get_neighbors(N_ROWS, N_COLS, row, col):
                    if matrix[nr][nc] == LAND_DEF:
                        queue.append((nr, nc))
                        matrix[nr][nc] = WATER_DEF

            return island_area

        max_island_area = 0
        for i in range(N_ROWS):
            for j in range(N_COLS):
                if matrix[i][j] == LAND_DEF:
                    matrix[i][j] = WATER_DEF
                    max_island_area = max(max_island_area, bfs(i, j))

        return max_island_area

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
        sol.maxAreaOfIsland(
            [
                [0, 0, 1, 0, 0],
                [0, 1, 1, 0, 1],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
            ]
        )
        == 7
    )

    assert (
        sol.maxAreaOfIsland(
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ]
        )
        == 25
    )

    print("All test cases passed.")
