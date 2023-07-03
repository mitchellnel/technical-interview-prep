class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def climb(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n - 1) + climb(n - 2)
                return memo[n]

        return climb(n)


def main():
    soln = Solution()

    print(f"climbStairs(2) = {soln.climbStairs(2)}")
    print(f"climbStairs(3) = {soln.climbStairs(3)}")
    print(f"climbStairs(10) = {soln.climbStairs(10)}")


main()
