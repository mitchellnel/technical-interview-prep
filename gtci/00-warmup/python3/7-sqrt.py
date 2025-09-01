def mySqrt(x: int) -> int:
    if x < 2:
        return x

    left = 2
    right = x // 2

    while left <= right:
        mid = left + (right - left) // 2
        num = mid * mid

        if num < x:
            left = mid + 1
        elif num > x:
            right = mid - 1
        else:
            return mid

    return right


if __name__ == "__main__":
    assert mySqrt(4) == 2
    assert mySqrt(8) == 2
    assert mySqrt(0) == 0
    assert mySqrt(1) == 1
    print("All test cases passed.")
