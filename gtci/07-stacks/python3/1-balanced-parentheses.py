class Solution:
    def isValid(self, s):
        stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if char == ")" and top != "(":
                    return False
                elif char == "]" and top != "[":
                    return False
                elif char == "}" and top != "{":
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()

    assert sol.isValid("()") == True
    assert sol.isValid("()[]{}") == True
    assert sol.isValid("(]") == False
    assert sol.isValid("([)]") == False
    assert sol.isValid("{[]}") == True
    assert sol.isValid("}") == False

    print("All test cases passed.")
