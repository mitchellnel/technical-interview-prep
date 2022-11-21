# O(hw) time | O(hw) space
def removeIslands(matrix):
    border_ones = [[False for _ in row] for row in matrix]

    # find all ones connected to border
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            row_is_border = row == 0 or row == len(matrix) - 1
            col_is_border = col == 0 or col == len(matrix[row]) - 1
            is_border = row_is_border or col_is_border
            if not is_border:
                continue

            if matrix[row][col] != 1:
                continue

            find_border_ones(matrix, row, col, border_ones)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if border_ones[row][col]:
                continue

            matrix[row][col] = 0

    return matrix


def find_border_ones(matrix, row, col, border_ones):
    stack = [(row, col)]
    visited = []

    while len(stack) > 0:
        curr = stack.pop()
        i, j = curr

        if border_ones[i][j]:
            continue

        border_ones[i][j] = True

        neighbours = get_neighbours(matrix, i, j)
        for neighbour in neighbours:
            r, c = neighbour
            if matrix[r][c] != 1:
                continue
            stack.append(neighbour)


def get_neighbours(matrix, row, col):
    neighbours = []

    num_rows = len(matrix)
    num_cols = len(matrix[row])

    if row - 1 >= 0:
        neighbours.append((row - 1, col))
    if row + 1 < num_rows:
        neighbours.append((row + 1, col))
    if col - 1 >= 0:
        neighbours.append((row, col - 1))
    if col + 1 < num_cols:
        neighbours.append((row, col + 1))

    return neighbours
