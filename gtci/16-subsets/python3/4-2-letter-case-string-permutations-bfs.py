from collections import deque


class Solution:
    def findLetterCaseStringPermutations(self, s):
        queue = deque()
        queue.append("")

        for char in s:
            n = len(queue)
            for _ in range(n):
                permutation = queue.popleft()

                if char.isalpha():
                    queue.append(permutation + char.lower())
                    queue.append(permutation + char.upper())
                else:
                    queue.append(permutation + char)

        return list(queue)

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
