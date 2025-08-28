from typing import List, Tuple


class Solution:
    def __init__(self):
        self.LAND_DEF = "1"
        self.WATER_DEF = "0"
        self.EXPLORED_DEF = "2"

    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        n_islands = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == self.LAND_DEF:
                    self.exploreIsland(grid, r, c)
                    n_islands += 1

        return n_islands

    def exploreIsland(self, grid: List[List[str]], start_row: int, start_col: int):
        stack = [(start_row, start_col)]
        visited = []

        while len(stack) > 0:
            curr_row, curr_col = stack.pop()

            if (curr_row, curr_col) in visited:
                continue

            if grid[curr_row][curr_col] == self.LAND_DEF:
                grid[curr_row][curr_col] = self.EXPLORED_DEF

            land_neighbours = self.getLandNeighbours(grid, curr_row, curr_col)
            for neighbour in land_neighbours:
                stack.append(neighbour)

    def getLandNeighbours(
        self, grid: List[List[str]], row: int, col: int
    ) -> List[Tuple[int, int]]:
        land_neighbours = []
        n_rows = len(grid)
        n_cols = len(grid[0])

        if row - 1 >= 0 and grid[row - 1][col] == self.LAND_DEF:
            land_neighbours.append((row - 1, col))
        if row + 1 < n_rows and grid[row + 1][col] == self.LAND_DEF:
            land_neighbours.append((row + 1, col))
        if col - 1 >= 0 and grid[row][col - 1] == self.LAND_DEF:
            land_neighbours.append((row, col - 1))
        if col + 1 < n_cols and grid[row][col + 1] == self.LAND_DEF:
            land_neighbours.append((row, col + 1))

        return land_neighbours
