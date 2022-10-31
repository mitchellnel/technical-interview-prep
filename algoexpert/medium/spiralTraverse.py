# O(n) time | O(n) space
def spiralTraverse(array):
    spiral = []

    start_row = 0
    end_row = len(array) - 1

    start_col = 0
    end_col = len(array[0]) - 1

    while start_row <= end_row and start_col <= end_col:
        # top row
        for i in range(start_col, end_col + 1):
            spiral.append(array[start_row][i])

        # right col
        for i in range(start_row + 1, end_row + 1):
            spiral.append(array[i][end_col])

        # bottom row
        for i in reversed(range(start_col, end_col)):
            # handle the case where there's a single row in the middle of the matrix
            # in this case, we just break to avoid double-counting
            if start_row == end_row:
                break
            spiral.append(array[end_row][i])

        # left col
        for i in reversed(range(start_row + 1, end_row)):
            # handle the case where there's a single col in the middle of the matrix
            # in this case, we just break to avoid double-counting
            if start_col == end_col:
                break
            spiral.append(array[i][start_col])

        # mutate perimeter values
        start_row += 1
        end_row -= 1

        start_col += 1
        end_col -= 1

    return spiral
