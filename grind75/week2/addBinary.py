class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_idx = len(a) - 1
        b_idx = len(b) - 1

        carry = 0
        result = ""

        while a_idx >= 0 or b_idx >= 0 or carry:
            if a_idx >= 0:
                carry += int(a[a_idx])
                a_idx -= 1

            if b_idx >= 0:
                carry += int(b[b_idx])
                b_idx -= 1

            # prepend
            result = str(carry % 2) + result
            carry //= 2

        return result


def main():
    soln = Solution()

    print(f"11 + 1 = {soln.addBinary('11', '1')}")
    print(f"1010 + 1011 = {soln.addBinary('1010', '1011')}")


main()
