class Solution:
    def __init__(self):
        self.OPERATORS = ["+", "-", "*"]

    def diffWaysToEvaluateExpression(self, input):
        """
        Time: O(n * 2^n) -- there are 2^(n-1) ways to add parentheses
        Space: O(n * 2^n) -- the memo dictionary can store up to 2^(n-1) keys,
        """
        memo = {}

        def dfs(expr):
            # base case -- memoised
            if expr in memo:
                return memo[expr]

            # base case -- no operators
            if not any(char in self.OPERATORS for char in expr):
                return [int(expr)]

            results = []

            # split at every operator
            for i, char in enumerate(expr):
                if char in self.OPERATORS:
                    left_vals = dfs(expr[:i])
                    right_vals = dfs(expr[i + 1 :])

                    for lhs in left_vals:
                        for rhs in right_vals:
                            if char == "+":
                                results.append(lhs + rhs)
                            elif char == "-":
                                results.append(lhs - rhs)
                            elif char == "*":
                                results.append(lhs * rhs)

            memo[expr] = results
            return results

        return dfs(input)


if __name__ == "__main__":
    sol = Solution()

    assert sorted(sol.diffWaysToEvaluateExpression("1+2*3")) == sorted([7, 9])
    assert sorted(sol.diffWaysToEvaluateExpression("2*3-4*5")) == sorted(
        [-34, -14, -10, -10, 10]
    )

    print("All test cases passed.")
