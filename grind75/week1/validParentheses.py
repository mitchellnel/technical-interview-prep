class Solution:
    def isValid(self, s: str) -> bool:
        # idea: pop stack to find matching opening bracket when we find a
        #       closing bracket
        OPENING = ['(', '[', '{']
        CLOSING = [')', ']', '}']

        MATCHING = {')': '(', ']': '[', '}': '{'}

        stack = []
        for char in s:
            if char in CLOSING and len(stack) == 0:
                return False
            elif char in CLOSING and MATCHING[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0

def main():
    soln = Solution()
    print("(): " + str(soln.isValid("()")))
    print("()[]{}: " + str(soln.isValid("()[]{}")))
    print("(]: " + str(soln.isValid("(]")))

main()