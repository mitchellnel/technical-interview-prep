def isHappyNumber(num):
    slow, fast = num, num

    while True:
        # slow pointer moves one step
        slow = findSquareSum(slow)

        # fast pointer moves two steps
        fast = findSquareSum(findSquareSum(fast))

        if slow == fast:
            # found the cycle
            break

    # see if the cycle is stuck on the number 1
    return slow == 1


def findSquareSum(num):
    square_sum = 0
    while num > 0:
        digit = num % 10
        square_sum += digit**2
        num //= 10

    return square_sum


def main():
    print(isHappyNumber(23))
    print(isHappyNumber(12))


main()
