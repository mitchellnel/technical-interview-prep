def subarray_averages(k, array):
    soln = []

    for i in range(0, len(array) - k + 1):
        sum = 0
        for j in range(i, i + k):
            sum += array[j]
        avg = sum / k
        soln.append(avg)

    return soln


def main():
    result = subarray_averages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
