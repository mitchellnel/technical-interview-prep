def flood_fill(matrix, starting, new_colour):
    start_row, start_col = starting

    start_colour = matrix[start_row][start_col]

    fill_dfs(matrix, start_colour, start_row, start_col, new_colour)

    return matrix


def fill_dfs(matrix, start_colour, row, col, replace_colour):
    height = len(matrix)
    width = len(matrix[0])

    # base cases - cell out of bounds, or cell is not colour to replace
    if row < 0 or row >= height:
        return
    if col < 0 or col >= width:
        return
    if matrix[row][col] != start_colour:
        return

    # change the colour
    matrix[row][col] = replace_colour

    # visit vertical and horizontal neighbours
    fill_dfs(matrix, start_colour, row - 1, col, replace_colour)  # up
    fill_dfs(matrix, start_colour, row + 1, col, replace_colour)  # down
    fill_dfs(matrix, start_colour, row, col - 1, replace_colour)  # left
    fill_dfs(matrix, start_colour, row, col + 1, replace_colour)  # right
