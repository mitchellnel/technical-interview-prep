class Solution:
    def findLetterCaseStringPermutations(self, s):
        """
        Time: O(n * 2^k) -- takes O(n) to build a permutation, and there are 2^k permutations
        Space: O(n) -- recursive stack
        """
        s_list = list(s)

        permutations = []

        n = len(s)

        def backtrack(start):
            if start == n:
                permutations.append("".join(s_list))
                return

            if not s_list[start].isalpha():
                backtrack(start + 1)
                return

            # recurse with original case
            backtrack(start + 1)

            # change case
            orig = s_list[start]
            s_list[start] = self.convert_case(s_list[start])

            # recurse with changed case
            backtrack(start + 1)

            # backtrack by restoring case
            s_list[start] = orig

        backtrack(0)
        return permutations

    def convert_case(self, char):
        return char.lower() if char.isupper() else char.upper()


if __name__ == "__main__":
    sol = Solution()

    assert set(sol.findLetterCaseStringPermutations("a1b2")) == set(
        ["a1b2", "a1B2", "A1b2", "A1B2"]
    )
    assert set(sol.findLetterCaseStringPermutations("3z4")) == set(["3z4", "3Z4"])
    assert set(sol.findLetterCaseStringPermutations("12345")) == set(["12345"])

    print("All test cases passed.")
