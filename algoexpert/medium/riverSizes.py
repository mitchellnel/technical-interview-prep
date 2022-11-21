# O(wh) time | O(wh) space
def riverSizes(matrix):
    sizes = []
    visited = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i, j) in visited:
                continue
            if matrix[i][j] == 1:
                traverse_river(matrix, i, j, sizes, visited)

    return sizes


def traverse_river(matrix, r, c, sizes, visited):
    river_size = 0
    queue = [(r, c)]

    while queue:
        curr = queue.pop()

        if curr in visited:
            continue

        visited.append(curr)

        i, j = curr

        if matrix[i][j] != 1:
            continue
        river_size += 1

        queue += get_unvisited_neighbours(matrix, i, j, visited)

    if river_size > 0:
        sizes.append(river_size)


def get_unvisited_neighbours(matrix, r, c, visited):
    unvisited = []
    neighbours = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]

    for neighbour in neighbours:
        if neighbour[0] < 0 or neighbour[0] > len(matrix) - 1:
            continue
        else:
            if neighbour[1] < 0 or neighbour[1] > len(matrix[r]) - 1:
                continue

        if neighbour in visited:
            continue

        unvisited.append(neighbour)

    return unvisited
