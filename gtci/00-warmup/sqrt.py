def mySqrt(x):
    # base case -- return x if it is 0 or 1
    if x < 2:
        return x

    # initialise left and right pointers
    left, right = 2, x // 2
    mid = 0

    # use int to store result of mid * mid
    num = 0

    # binary search for the square root
    while left <= right:
        mid = left + (right - left) // 2
        num = mid * mid

        if num > x:
            right = mid - 1
        elif num < x:
            left = mid + 1
        else:
            return mid

    return right


def main():
    input1 = 4
    expectedOutput1 = 2
    result1 = mySqrt(input1)
    print(result1 == expectedOutput1)  # Expected output: True

    input2 = 8
    expectedOutput2 = 2
    result2 = mySqrt(input2)
    print(result2 == expectedOutput2)  # Expected output: True

    input4 = 2
    expectedOutput4 = 1
    result4 = mySqrt(input4)
    print(result4 == expectedOutput4)  # Expected output: True

    input5 = 3
    expectedOutput5 = 1
    result5 = mySqrt(input5)
    print(result5 == expectedOutput5)  # Expected output: True

    input6 = 15
    expectedOutput6 = 3
    result6 = mySqrt(input6)
    print(result6 == expectedOutput6)  # Expected output: True


main()
