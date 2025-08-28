from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea: at each step work out the max possible profit
        # we will use a buy price (a minimum) that occurs strictly
        #   before or including the day for which we're working out
        #   the max profit
        curr_min = float("inf")
        max_profit = 0

        for idx, price in enumerate(prices):
            curr_min = min(curr_min, price)

            max_profit = max(max_profit, price - curr_min)

        return max_profit


def main():
    soln = Solution()

    print("Prices: [7,1,5,3,6,4]")
    print(f"Max Profit: {soln.maxProfit([7,1,5,3,6,4])}")

    print()

    print("Price: [7,6,4,3,1]")
    print(f"Max Profit: {soln.maxProfit([7,6,4,3,1])}")


main()
