class Solution:
    def findLetterCaseStringPermutations(self, s):
        permutations = []

        def dfs(index, path):
            if index == len(s):
                permutations.append(path[:])
                return

            char = s[index]
            if char.isalpha():
                dfs(index + 1, path + char.lower())
                dfs(index + 1, path + char.upper())
            else:
                dfs(index + 1, path + char)

        dfs(0, "")
        return permutations


if __name__ == "__main__":
    sol = Solution()

    assert set(sol.findLetterCaseStringPermutations("a1b2")) == set(
        ["a1b2", "a1B2", "A1b2", "A1B2"]
    )
    assert set(sol.findLetterCaseStringPermutations("3z4")) == set(["3z4", "3Z4"])
    assert set(sol.findLetterCaseStringPermutations("12345")) == set(["12345"])

    print("All test cases passed.")
