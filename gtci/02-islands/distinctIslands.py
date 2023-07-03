WATER_DEF = 0
LAND_DEF = 1


def count_distinct_islands(matrix):
    traversal_orders = set()

    height = len(matrix)
    width = len(matrix[0])

    # traverse element-by-element
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == LAND_DEF:
                traversal_string = get_traversal_string(matrix, row, col, "O")

                traversal_orders.add(traversal_string)

    return len(traversal_orders)


def get_traversal_string(matrix, row, col, movement):
    height = len(matrix)
    width = len(matrix[0])

    # base cases - out of bounds or water
    if row < 0 or row >= height:
        return ""
    if col < 0 or col >= width:
        return ""
    if matrix[row][col] == WATER_DEF:
        return ""

    # mark as visited
    matrix[row][col] = WATER_DEF

    # explore rest of the island, and return total size
    return (
        movement
        + get_traversal_string(matrix, row - 1, col, "U")
        + get_traversal_string(matrix, row + 1, col, "D")
        + get_traversal_string(matrix, row, col - 1, "L")
        + get_traversal_string(matrix, row, col + 1, "R")
    )
