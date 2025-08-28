def find_missing_number(array):
    n = len(array) + 1

    x1 = 1
    for i in range(2, n + 1):
        x1 ^= i

    x2 = array[0]
    for i in range(1, len(array)):
        x2 ^= array[i]

    return x1 ^ x2


def main():
    arr = [1, 5, 2, 6, 4]
    print("Missing number is: " + str(find_missing_number(arr)))


main()
