WATER_DEF = 0
LAND_DEF = 1

VISITED_DEF = 2


def count_closed_islands(matrix):
    n_closed_islands = 0

    height = len(matrix)
    width = len(matrix[0])

    # traverse element-by-element
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == LAND_DEF:
                if is_island_closed(matrix, row, col):
                    n_closed_islands += 1

    return n_closed_islands


def is_island_closed(matrix, row, col):
    height = len(matrix)
    width = len(matrix[0])

    # base case - out of bounds, return false, water or visited, return true
    if row < 0 or row >= height:
        return False
    if col < 0 or col >= width:
        return False
    if matrix[row][col] == WATER_DEF or matrix[row][col] == VISITED_DEF:
        return True

    # mark as visited
    matrix[row][col] = VISITED_DEF

    # explore neighbours
    up_res = is_island_closed(matrix, row - 1, col)
    down_res = is_island_closed(matrix, row + 1, col)
    left_res = is_island_closed(matrix, row, col - 1)
    right_res = is_island_closed(matrix, row, col + 1)

    # return AND of their result
    return up_res and down_res and left_res and right_res
