class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if len(s) == 0:
            return 0

        sign = -1 if s[0] == "-" else 1
        s = s[1:] if s[0] == "-" or s[0] == "+" else s

        num_int = 0
        for char in s:
            if not char.isdigit():
                break

            num_int = num_int * 10 + ord(char) - ord("0")

        return max(-(2**31), min(sign * num_int, 2**31 - 1))


def main():
    soln = Solution()

    print(soln.myAtoi("42"))
    print(soln.myAtoi("-42"))
    print(soln.myAtoi("4193 with words"))


main()
