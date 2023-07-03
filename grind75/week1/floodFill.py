from typing import List, Tuple


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        start_colour = image[sr][sc]

        queue = [(sr, sc)]
        visited = []
        while len(queue) > 0:
            row, col = queue.pop(0)

            # add to visited
            visited.append((row, col))

            # replace if correct colour
            if image[row][col] == start_colour:
                image[row][col] = color

            # find neighbours of correct colour
            neighbours = self.find_neighbours(visited, image, row, col, start_colour)
            for neighbour in neighbours:
                queue.append(neighbour)

        return image

    def find_neighbours(
        self,
        visited: List[Tuple[int, int]],
        image: List[List[int]],
        row: int,
        col: int,
        color: int,
    ):
        n_rows = len(image)
        n_cols = len(image[0])

        neighbours = []
        if (
            row - 1 >= 0
            and image[row - 1][col] == color
            and (row - 1, col) not in visited
        ):
            neighbours.append((row - 1, col))
        if (
            row + 1 < n_rows
            and image[row + 1][col] == color
            and (row + 1, col) not in visited
        ):
            neighbours.append((row + 1, col))
        if (
            col - 1 >= 0
            and image[row][col - 1] == color
            and (row, col - 1) not in visited
        ):
            neighbours.append((row, col - 1))
        if (
            col + 1 < n_cols
            and image[row][col + 1] == color
            and (row, col + 1) not in visited
        ):
            neighbours.append((row, col + 1))

        return neighbours


def main():
    soln = Solution()
    print(f"image = [[1,1,1],[1,1,0],[1,0,1]]; sr = 1; sc = 1; color = 2")
    print(f"{soln.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)}")

    print(f"image = [[0,0,0],[0,0,0]]; sr = 0; sc = 0; color = 0")
    print(f"{soln.floodFill([[0,0,0],[0,0,0]], 0, 0, 0)}")


main()
