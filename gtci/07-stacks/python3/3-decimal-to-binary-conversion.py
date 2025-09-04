class Solution:
    def decimalToBinary(self, num):
        if num == 0:
            return "0"

        stack = []

        while num != 0:
            quotient = num // 2
            remainder = num % 2

            stack.append(remainder)
            num = quotient

        return "".join(str(char) for char in reversed(stack))


if __name__ == "__main__":
    sol = Solution()

    assert sol.decimalToBinary(0) == "0"
    assert sol.decimalToBinary(5) == "101"
    assert sol.decimalToBinary(10) == "1010"
    assert sol.decimalToBinary(255) == "11111111"

    print("All test cases passed.")
