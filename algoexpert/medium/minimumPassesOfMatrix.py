# O(hw) time | O(hw) space
def minimumPassesOfMatrix(matrix):
    passes = flip_negatives(matrix)
    return passes - 1 if not contains_negatives(matrix) else -1


def flip_negatives(matrix):
    passes = 0

    current_pass_queue = []
    next_pass_queue = get_positive_positions(matrix)

    while len(next_pass_queue) > 0:
        current_pass_queue = next_pass_queue
        next_pass_queue = []

        while len(current_pass_queue) > 0:
            curr = current_pass_queue.pop(0)

            r, c = curr
            neighbours = get_neighbours(matrix, r, c)

            for neighbour in neighbours:
                nei_r, nei_c = neighbour
                if matrix[nei_r][nei_c] < 0:
                    matrix[nei_r][nei_c] *= -1
                    next_pass_queue.append((nei_r, nei_c))

        passes += 1

    return passes


def get_positive_positions(matrix):
    positions = []

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] > 0:
                positions.append((r, c))

    return positions


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


def contains_negatives(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] < 0:
                return True

    return False
