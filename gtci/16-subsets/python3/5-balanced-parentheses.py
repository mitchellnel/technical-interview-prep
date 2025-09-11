class Solution:
    def generateValidParentheses(self, num):
        result = []

        def backtrack(total_paren_count, open_paren_count, path):
            # base case
            if total_paren_count == num * 2:
                result.append(path)
                return

            # at every step we have two choices:
            # - open a parentheses block
            # - close a parentheses if we've one open already
            if open_paren_count > 0:
                backtrack(total_paren_count + 1, open_paren_count - 1, path + ")")

            if total_paren_count + open_paren_count < num * 2:
                backtrack(total_paren_count + 1, open_paren_count + 1, path + "(")

        backtrack(0, 0, "")
        return result


if __name__ == "__main__":
    sol = Solution()

    assert set(sol.generateValidParentheses(2)) == set(["(())", "()()"])
    assert set(sol.generateValidParentheses(3)) == set(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )

    print("All test cases passed.")
