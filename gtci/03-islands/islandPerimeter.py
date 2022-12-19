WATER_DEF = 0
LAND_DEF = 1

VISITED_DEF = 2


def island_perimeter(matrix):
    height = len(matrix)
    width = len(matrix[0])

    perimeter = 0

    # traverse element-by-element
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == LAND_DEF:
                perimeter = get_island_perimeter(matrix, row, col)
                break

    return perimeter


def get_island_perimeter(matrix, row, col):
    height = len(matrix)
    width = len(matrix[0])

    # base case - out of bounds or water, return 1 (the contributing perimeter); visited, return 0
    if row < 0 or row >= height:
        return 1
    if col < 0 or col >= width:
        return 1
    if matrix[row][col] == WATER_DEF:
        return 1
    if matrix[row][col] == VISITED_DEF:
        return 0

    # mark cell as visited
    matrix[row][col] = VISITED_DEF

    # explore neighbours
    up_perim = get_island_perimeter(matrix, row - 1, col)
    down_perim = get_island_perimeter(matrix, row + 1, col)
    left_perim = get_island_perimeter(matrix, row, col - 1)
    right_perim = get_island_perimeter(matrix, row, col + 1)

    return up_perim + down_perim + left_perim + right_perim
