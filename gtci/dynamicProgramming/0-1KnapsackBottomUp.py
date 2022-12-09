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

        dp = [[0 for _ in range(self.capacity + 1)] for _ in range(n)]

        # populate the capacity = 0 columns
        # with 0 capacity, we have 0 profit
        for i in range(n):
            dp[i][0] = 0

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(1, self.capacity + 1):
            if self.weights[0] <= c:
                dp[0][c] = self.profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(1, self.capacity + 1):
                profit1, profit2 = 0, 0

                # if the item is not more than the capacity, include it
                if self.weights[i] <= c:
                    profit1 = self.profits[i] + dp[i - 1][c - self.weights[i]]

                # exclude the item
                profit2 = dp[i - 1][c]

                # take the maximum
                dp[i][c] = max(profit1, profit2)

        # maximum profit will be the bottom right answer
        self._print_selected_items(dp)
        return dp[n - 1][self.capacity]

    def _print_selected_items(self, dp):
        print("Selected weights:")

        n = len(self.weights)

        total_profit = dp[n - 1][self.capacity]
        remaining_capacity = self.capacity

        for i in range(n - 1, 0, -1):
            if total_profit != dp[i - 1][remaining_capacity]:
                print(str(self.weights[i]) + " ", end="")

                remaining_capacity -= self.weights[i]
                total_profit -= self.profits[i]

        if total_profit != 0:
            print(str(self.weights[0]) + " ", end="")
        print()


def main():
    knapsack1 = Knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5)
    print(knapsack1.solve_knapsack())

    knapsack2 = Knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)
    print(knapsack2.solve_knapsack())

    knapsack3 = Knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)
    print(knapsack3.solve_knapsack())


main()
