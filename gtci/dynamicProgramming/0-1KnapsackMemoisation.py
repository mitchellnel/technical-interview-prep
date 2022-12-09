def solve_knapsack(profits, weights, capacity):
    # create a two dimensional array for memoisation
    # each element is initialised to -1
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]

    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, current_index):
    # base case
    if capacity <= 0 or current_index >= len(profits):
        return 0

    # if we have already solved a similar problem, then return the result from our dp array
    if dp[current_index][capacity] != -1:
        return dp[current_index][capacity]

    # else, solve as normal
    # recursive call after choosing element at current_index
    # if the weight of the element at current_index exceed the capacity, we shouldn't process this
    current_index_weight = weights[current_index]
    profit1 = 0
    if current_index_weight <= capacity:
        profit1 = profits[current_index] + knapsack_recursive(
            dp, profits, weights, capacity - current_index_weight, current_index + 1
        )

    # recursive call after skipping element at current_index
    profit2 = knapsack_recursive(dp, profits, weights, capacity, current_index + 1)

    # record result in our dp array
    dp[current_index][capacity] = max(profit1, profit2)
    return dp[current_index][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
