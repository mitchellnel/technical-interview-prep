WATER_DEF = 0
LAND_DEF = 1


def biggest_island_DFS(matrix):
    biggest_island = None

    height = len(matrix)
    width = len(matrix[0])

    # traverse element-by-element
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == LAND_DEF:
                island_area = get_island_area_DFS(matrix, row, col)

                if biggest_island is None:
                    biggest_island = island_area
                else:
                    biggest_island = max(biggest_island, island_area)

    return biggest_island


def get_island_area_DFS(matrix, row, col):
    height = len(matrix)
    width = len(matrix[0])

    # base cases -- cell is out of bounds or is not land
    if row < 0 or row >= height:
        return 0
    if col < 0 or col >= width:
        return 0
    if matrix[row][col] != LAND_DEF:
        return 0

    # mark as visited
    matrix[row][col] = WATER_DEF

    # get area from rest of the island
    island_area = (
        1
        + get_island_area_DFS(matrix, row - 1, col)
        + get_island_area_DFS(matrix, row + 1, col)
        + get_island_area_DFS(matrix, row, col - 1)
        + get_island_area_DFS(matrix, row, col + 1)
    )

    return island_area


def biggest_island_BFS(matrix):
    biggest_island = None

    height = len(matrix)
    width = len(matrix[0])

    # traverse element-by-element
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == LAND_DEF:
                island_area = get_island_area_BFS(matrix, row, col)

                if biggest_island is None:
                    biggest_island = island_area
                else:
                    biggest_island = max(biggest_island, island_area)

    return biggest_island


def get_island_area_BFS(matrix, row, col):
    island_area = 0

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

        # mark as visited
        matrix[curr_row][curr_col] = WATER_DEF

        # increase area
        island_area += 1

        # enqueue neighbours
        queue.append((curr_row - 1, curr_col))  # up
        queue.append((curr_row + 1, curr_col))  # down
        queue.append((curr_row, curr_col - 1))  # left
        queue.append((curr_row, curr_col + 1))  # right

    return island_area
