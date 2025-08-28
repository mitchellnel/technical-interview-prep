from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.EMPTY_DEF = 0
        self.FRESH_DEF = 1
        self.ROTTEN_DEF = 2

    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        rotten_queue = deque()

        n_rows = len(grid)
        n_cols = len(grid[0])
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == self.FRESH_DEF:
                    fresh_count += 1
                elif grid[r][c] == self.ROTTEN_DEF:
                    rotten_queue.append((r, c))

        minutes_passed = 0

        # while there are still rotten oranges in the queue, and there
        #   are still fresh oranges, keep searching
        while len(rotten_queue) > 0 and fresh_count > 0:
            # BFS is level-by-level, so we can increment minutes_passed
            minutes_passed += 1

            # process rotten oranges on the current level
            for _ in range(len(rotten_queue)):
                curr_row, curr_col = rotten_queue.popleft()

                # visit all 4-directionally adjacent cells
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_row = curr_row + dx
                    new_col = curr_col + dy

                    # ignore cell if it is out of grid boundaries
                    if (
                        new_row < 0
                        or new_row >= n_rows
                        or new_col < 0
                        or new_col >= n_cols
                    ):
                        continue

                    # ignore cell if it is empty or it is another rotten orange
                    if (
                        grid[new_row][new_col] == self.EMPTY_DEF
                        or grid[new_row][new_col] == self.ROTTEN_DEF
                    ):
                        continue

                    # else, we have a fresh orange, so rot it
                    fresh_count -= 1
                    grid[new_row][new_col] = self.ROTTEN_DEF

                    # add the newly rotten orange to the queue
                    rotten_queue.append((new_row, new_col))

        # only return minutes_passed if there are no fresh oranges left
        return minutes_passed if fresh_count == 0 else -1


def main():
    soln = Solution()

    print(
        f"Time to fully rot [[2,1,1],[1,1,0],[0,1,1]] is {soln.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])}"
    )
    print(
        f"Time to fully rot [[2,1,1],[0,1,1],[1,0,1]] is {soln.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])}"
    )
    print(f"Time to fully rot [[0,2]] is {soln.orangesRotting([[0,2]])}")


main()
