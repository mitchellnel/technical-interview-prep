class Solution:
    def hasCycle(self, matrix):
        N_ROWS = len(matrix)
        N_COLS = len(matrix[0])

        visited = [[False for _ in range(N_COLS)] for _ in range(N_ROWS)]

        def has_cycle_bfs(start_row, start_col):
            letter = matrix[start_row][start_col]
            stack = [(start_row, start_col, None)]

            while stack:
                row, col, parent = stack.pop()

                for nr, nc in self.get_neighbors(N_ROWS, N_COLS, row, col):
                    if (
                        matrix[nr][nc] == letter
                        and visited[nr][nc]
                        and (nr, nc) != parent
                    ):
                        return True

                    if (
                        matrix[nr][nc] == letter
                        and not visited[nr][nc]
                        and (nr, nc) != parent
                    ):
                        visited[nr][nc] = True
                        stack.append((nr, nc, (row, col)))

            return False

        for i in range(N_ROWS):
            for j in range(N_COLS):
                if not visited[i][j]:
                    visited[i][j] = True
                    if has_cycle_bfs(i, j):
                        return True

        return False

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

    assert not sol.hasCycle(
        [
            ["a", "b", "b"],
            ["b", "z", "b"],
            ["b", "b", "a"],
        ]
    )

    assert not sol.hasCycle(
        [
            ["a", "b", "b"],
            ["b", "a", "b"],
            ["b", "b", "a"],
        ]
    )

    assert sol.hasCycle(
        [
            ["a", "a", "a", "a"],
            ["a", "b", "b", "a"],
            ["a", "b", "b", "a"],
            ["a", "a", "a", "a"],
        ]
    )

    print("All test cases passed.")
