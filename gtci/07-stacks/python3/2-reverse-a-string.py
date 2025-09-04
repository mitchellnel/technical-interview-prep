class Solution:
    def reverseString(self, s):
        stack = []

        for char in s:
            stack.append(char)

        reversed_s = ""

        while len(stack) > 0:
            reversed_s += stack.pop()

        return reversed_s


if __name__ == "__main__":
    sol = Solution()

    assert sol.reverseString("hello") == "olleh"
    assert sol.reverseString("world") == "dlrow"
    assert sol.reverseString("Python") == "nohtyP"

    print("All test cases passed.")
