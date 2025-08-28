class Knapsack:
    def __init__(self, profits, weights, capacity):
        self.profits = profits
        self.weights = weights
        self.capacity = capacity

    def solve_knapsack(self):
        # base case
        n = len(self.profits)
        if self.capacity <= 0 or n == 0 or len(self.weights) != n:
            return 0

        # we only need one previous row to find the optimal solution, so we just need 2 rows
        # so now when we do `i` we will do `i % 2` and instead of `i - 1` we will do `(i - 1) % 2`
        dp = [[0 for _ in range(self.capacity + 1)] for _ in range(2)]

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(1, self.capacity + 1):
            if self.weights[0] <= c:
                dp[0][c] = dp[1][c] = self.profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(1, self.capacity + 1):
                profit1, profit2 = 0, 0

                # if the item is not more than the capacity, include it
                if self.weights[i] <= c:
                    profit1 = self.profits[i] + dp[(i - 1) % 2][c - self.weights[i]]

                # exclude the item
                profit2 = dp[(i - 1) % 2][c]

                # take the maximum
                dp[i % 2][c] = max(profit1, profit2)

        # maximum profit will be the bottom right answer
        return dp[(n - 1) % 2][self.capacity]


def main():
    knapsack1 = Knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5)
    print(knapsack1.solve_knapsack())

    knapsack2 = Knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)
    print(knapsack2.solve_knapsack())

    knapsack3 = Knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)
    print(knapsack3.solve_knapsack())


main()
