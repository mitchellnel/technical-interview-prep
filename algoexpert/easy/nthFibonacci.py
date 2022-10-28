# O(2^n) time | O(n) space
def getNthFib_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return getNthFib_recursive(n - 1) + getNthFib_recursive(n - 2)


# O(n) time | O(n) space
def getNthFib_dynamicProgramming(n, dp={1: 0, 2: 1}):
    if n in dp:
        return dp[n]

    dp[n] = getNthFib_dynamicProgramming(n - 1, dp) + getNthFib_dynamicProgramming(
        n - 2, dp
    )

    return dp[n]


# O(n) time | O(1) space
def getNthFib_iterative(n):
    last_two = [0, 1]
    counter = 3

    while counter <= n:
        next_fib = last_two[0] + last_two[1]

        last_two[0] = last_two[1]
        last_two[1] = next_fib

        counter += 1

    return last_two[1] if n > 1 else last_two[0]
