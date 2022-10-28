# O(n) time | O(n) space
def sortedSquaredArray(array):
    squares = [0 for _ in array]
    small = 0
    large = len(array) - 1

    for idx in reversed(range(len(array))):
        smallVal = array[small]
        largeVal = array[large]

        print(smallVal)
        print(largeVal)

        if abs(smallVal) > abs(largeVal):
            squares[idx] = smallVal**2
            small += 1
        else:
            squares[idx] = largeVal**2
            large -= 1

        print(squares)

    return squares
