def mySqrt(self, x: int) -> int:
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
    print(mySqrt(4))  # Output: 2
    print(mySqrt(8))  # Output: 2
    print(mySqrt(0))  # Output: 0
    print(mySqrt(1))  # Output: 1
