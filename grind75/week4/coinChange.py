from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1


def main():
    soln = Solution()

    print(
        f"Using coins [1,2,5], it takes a minimum of {soln.coinChange([1,2,5], 11)} to reach amount 11"
    )
    print(
        f"Using coins [2], it takes a minimum of {soln.coinChange([2], 3)} to reach amount 3"
    )
    print(
        f"Using coins [1], it takes a minimum of {soln.coinChange([1], 0)} to reach amount 0"
    )


main()
