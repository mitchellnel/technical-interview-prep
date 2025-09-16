class Solution:
    def bitwiseComplement(self, num):
        mask = 1
        while mask <= num:
            mask <<= 1
        mask -= 1

        return num ^ mask


if __name__ == "__main__":
    sol = Solution()

    assert sol.bitwiseComplement(5) == 2

    assert sol.bitwiseComplement(7) == 0

    assert sol.bitwiseComplement(10) == 5

    print("All test cases passed.")
