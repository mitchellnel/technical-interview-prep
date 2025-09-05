class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack and char == stack[-1][0] and k - 1 == stack[-1][1]:
                stack.pop()
            else:
                if stack and char == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([char, 1])

        return "".join([char * count for char, count in stack])


if __name__ == "__main__":
    sol = Solution()

    assert sol.removeDuplicates("abbbaaca", 3) == "ca"
    assert sol.removeDuplicates("abbaccaa", 3) == "abbaccaa"
    assert sol.removeDuplicates("abbacccaa", 3) == "abb"

    print("All test cases passed.")
