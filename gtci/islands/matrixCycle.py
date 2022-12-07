def matrix_cycle(matrix):
    height = len(matrix)
    width = len(matrix[0])

    visited = [[False for _ in range(width)] for _ in range(height)]

    # traverse element-by-element
    for row in range(height):
        for col in range(width):
            if not visited[row][col]:
                if find_cycle(matrix, visited, matrix[row][col], row, col, -1, -1):
                    return True

    return False


def find_cycle(matrix, visited, char, row, col, prev_row, prev_col):
    height = len(matrix)
    width = len(matrix[0])

    # base case - out of bounds, wrong character, or we've found a cell we already visited
    if row < 0 or row >= height:
        return False
    if col < 0 or col >= width:
        return False
    if matrix[row][col] != char:
        return False
    if visited[row][col]:
        return True

    # mark as visited
    visited[row][col] = True

    # traverse neighbours -- but don't traverse parent
    if row - 1 != prev_row and find_cycle(
        matrix, visited, char, row - 1, col, row, col
    ):
        return True
    if row + 1 != prev_row and find_cycle(
        matrix, visited, char, row + 1, col, row, col
    ):
        return True
    if col - 1 != prev_col and find_cycle(
        matrix, visited, char, row, col - 1, row, col
    ):
        return True
    if col + 1 != prev_col and find_cycle(
        matrix, visited, char, row, col + 1, row, col
    ):
        return True

    return False
