from typing import List


class Solution:
    def __init__(self):
        self.OPERATORS = ["+", "-", "*", "/"]

    def isOperator(self, token: str):
        return token in self.OPERATORS

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isOperator(token):
                right_operand = int(stack.pop())
                left_operand = int(stack.pop())

                result = None
                if token == "+":
                    result = left_operand + right_operand
                elif token == "-":
                    result = left_operand - right_operand
                elif token == "*":
                    result = left_operand * right_operand
                elif token == "/":
                    result = left_operand / right_operand

                stack.append(result)
            else:
                stack.append(token)

        result = int(stack.pop())
        return result


def main():
    soln = Solution()

    print(f"tokens = ['2','1','+','3','*'] --> {soln.evalRPN(['2','1','+','3','*'])}")
    print(f'tokens = ["4","13","5","/","+"] --> {soln.evalRPN(["4","13","5","/","+"])}')
    print(
        f'tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] --> {soln.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])}'
    )


main()
