class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if len(stack) > 0 and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()

    assert sol.removeDuplicates("abccba") == ""
    assert sol.removeDuplicates("foobar") == "fbar"
    assert sol.removeDuplicates("fooobar") == "fobar"
    assert sol.removeDuplicates("abcd") == "abcd"

    print("All test cases passed.")
