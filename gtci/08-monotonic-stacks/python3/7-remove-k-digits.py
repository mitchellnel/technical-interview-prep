class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        removed = 0
        for digit in num:
            while stack and removed < k and int(digit) < stack[-1]:
                stack.pop()
                removed += 1

            stack.append(int(digit))

        while removed < k:
            stack.pop()
            removed += 1

        result = ""
        for num in stack:
            if result == "" and num == 0:
                continue

            result += str(num)

        return result if result != "" else "0"


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeKdigits("1432219", 3) == "1219"
    assert sol.removeKdigits("10200", 1) == "200"
    assert sol.removeKdigits("10", 2) == "0"
    assert sol.removeKdigits("1234567890", 9) == "0"
    assert sol.removeKdigits("9876543210", 5) == "43210"

    print("All test cases passed.")
