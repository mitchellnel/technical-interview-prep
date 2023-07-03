def find_missing_number(array):
    n = len(array) + 1
    s1 = 0
    for i in range(1, n + 1):
        s1 += i

    for num in array:
        s1 -= num

    return s1


def main():
    arr = [1, 5, 2, 6, 4]
    print("Missing number is: " + str(find_missing_number(arr)))


main()
