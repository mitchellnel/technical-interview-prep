def find_single_number(array):
    x = array[0]
    for i in range(1, len(array)):
        x ^= array[i]

    return x


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

    arr = [7, 9, 7]
    print(find_single_number(arr))


main()
