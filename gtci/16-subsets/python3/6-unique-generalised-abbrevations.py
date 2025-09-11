class Solution:
    def generateGeneralizedAbbreviation(self, word):
        """
        Time: O(2^n * n) - we have 2 choices (abbreviate or not) for each of the n letters
        Space: O(n) - recursion stack
        """
        result = []

        def backtrack(index, path, count):
            # base case
            if index == len(word):
                if count > 0:
                    path += str(count)
                result.append(path)
                return

            # at every step we have two choices:
            # - append the letter
            # - append the number
            #   * if the preceding character is a number, add to it

            # to avoid string slicing, we will not commit a count until we are
            # choosing to commit a letter
            new_path = path
            if count > 0:
                new_path += str(count)
            backtrack(index + 1, new_path + word[index], 0)

            backtrack(index + 1, path, count + 1)

        backtrack(0, "", 0)
        return result


if __name__ == "__main__":
    sol = Solution()

    assert set(sol.generateGeneralizedAbbreviation("BAT")) == set(
        ["3", "2T", "1A1", "1AT", "B2", "B1T", "BA1", "BAT"]
    )
    assert set(sol.generateGeneralizedAbbreviation("code")) == set(
        [
            "4",
            "3e",
            "2d1",
            "2de",
            "1o2",
            "1o1e",
            "1od1",
            "1ode",
            "c3",
            "c2e",
            "c1d1",
            "c1de",
            "co2",
            "co1e",
            "cod1",
            "code",
        ]
    )

    print("All test cases passed.")
