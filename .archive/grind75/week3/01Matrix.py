from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n_rows = len(mat)
        n_cols = len(mat[0])

        soln = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

        queue = []
        visited = set()

        # element-wise traversal to look for 0s
        for r in range(n_rows):
            for c in range(n_cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        neighbouring_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # bfs to 1s
        while len(queue) > 0:
            curr_row, curr_col = queue.pop(0)
            for direction in neighbouring_dirs:
                new_row = curr_row + direction[0]
                new_col = curr_col + direction[1]

                if (
                    new_row >= 0
                    and new_col >= 0
                    and new_row < n_rows
                    and new_col < n_cols
                    and (new_row, new_col) not in visited
                ):
                    mat[new_row][new_col] = mat[curr_row][curr_col] + 1
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

        return mat


def main():
    soln = Solution()

    print(
        f"mat = [[0,0,0],[0,1,0],[0,0,0]] --> {soln.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])}"
    )

    print(
        f"mat = [[0,0,0],[0,1,0],[1,1,1]] --> {soln.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])}"
    )


main()
