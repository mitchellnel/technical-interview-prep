def flip_and_invert(matrix):
    # matrix is square
    n_cols = len(matrix)
    for row in matrix:
        for i in range((n_cols + 1) // 2):
            row[i], row[n_cols - i - 1] = row[n_cols - i - 1] ^ 1, row[i] ^ 1

    return matrix


def main():
    print(flip_and_invert([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_and_invert([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()
