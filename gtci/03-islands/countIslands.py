WATER_DEF = 0
LAND_DEF = 1


def count_islands_DFS(matrix):
    n_islands = 0

    height = len(matrix)
    width = len(matrix[0])

    # traverse through matrix element-by-element
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == LAND_DEF:
                # found a new island
                n_islands += 1

                # visit the full island
                visit_island_DFS(matrix, row, col)

    return n_islands


def visit_island_DFS(matrix, row, col):
    height = len(matrix)
    width = len(matrix[0])

    # base case - cell is out of bounds, or not land
    if row < 0 or row >= height:
        return
    if col < 0 or col >= width:
        return
    if matrix[row][col] != LAND_DEF:
        return

    # mark the cell as visited
    matrix[row][col] = WATER_DEF

    # visit horizontal and vertical neighbours
    visit_island_DFS(matrix, row - 1, col)  # up
    visit_island_DFS(matrix, row + 1, col)  # down
    visit_island_DFS(matrix, row, col - 1)  # left
    visit_island_DFS(matrix, row, col + 1)  # right


###


def count_islands_BFS(matrix):
    n_islands = 0

    height = len(matrix)
    width = len(matrix[0])

    # traverse through matrix element-by-element
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == LAND_DEF:
                # found a new island
                n_islands += 1

                # visit the full island
                visit_island_BFS(matrix, row, col)

    return n_islands


def visit_island_BFS(matrix, row, col):
    height = len(matrix)
    width = len(matrix[0])

    # use a queue for BFS
    queue = [(row, col)]

    # run until we run out of cells to look at - visited island fully
    while len(queue) > 0:
        curr_cell = queue.pop(0)

        curr_row, curr_col = curr_cell

        # check if cell is out of bounds, or not land
        if curr_row < 0 or curr_row >= height:
            continue
        if curr_col < 0 or curr_col >= width:
            continue
        if matrix[curr_row][curr_col] != LAND_DEF:
            continue

        # mark cell as visited
        matrix[curr_row][curr_col] = WATER_DEF

        # enqueue neighbours
        queue.append((curr_row - 1, curr_col))  # up
        queue.append((curr_row + 1, curr_col))  # down
        queue.append((curr_row, curr_col - 1))  # left
        queue.append((curr_row, curr_col + 1))  # right
