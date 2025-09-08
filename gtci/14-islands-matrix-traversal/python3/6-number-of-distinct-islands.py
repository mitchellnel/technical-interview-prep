from collections import deque


class Solution:
    def findDistinctIslandsDFS(self, matrix):
        WATER_DEF = 0
        LAND_DEF = 1

        N_ROWS = len(matrix)
        N_COLS = len(matrix[0])

        def bfs_traversal(start_row, start_col):
            queue = deque()
            queue.append((0, 0))  # pos relative to (start_row, start_col)

            traversal = []
            while queue:
                row, col = queue.popleft()

                traversal.append((row, col))

                row += start_row
                col += start_col

                for nr, nc in self.get_neighbors(N_ROWS, N_COLS, row, col):
                    if matrix[nr][nc] == LAND_DEF:
                        matrix[nr][nc] = WATER_DEF
                        queue.append((nr - start_row, nc - start_col))

            return tuple(traversal)

        traversals = set()
        for i in range(N_ROWS):
            for j in range(N_COLS):
                if matrix[i][j] == LAND_DEF:
                    matrix[i][j] = WATER_DEF
                    traversals.add(bfs_traversal(i, j))

        return len(traversals)

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
        sol.findDistinctIslandsDFS(
            [
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 1, 1],
                [0, 1, 0, 0, 0],
            ]
        )
        == 3
    )

    assert (
        sol.findDistinctIslandsDFS(
            [
                [1, 1, 0, 1, 1],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [1, 1, 0, 1, 0],
            ]
        )
        == 2
    )

    assert (
        sol.findDistinctIslandsDFS(
            [
                [1, 1, 0, 1, 1],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [1, 1, 0, 1, 1],
            ]
        )
        == 3
    )

    print("All test cases passed.")
