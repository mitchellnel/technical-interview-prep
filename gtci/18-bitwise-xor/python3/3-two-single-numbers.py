class Solution:
    def findSingleNumbers(self, nums):
        xor_all = 0
        for num in nums:
            xor_all ^= num

        # get rightmost set bit in xor_all using bit trick
        # use this to find a bit where the two numbers differ
        rightmost_set_bit = xor_all & -xor_all

        # sort the two numbers into two groups using their differing rightmost bit
        xor_1 = 0
        xor_2 = 0
        for num in nums:
            if num & rightmost_set_bit != 0:
                # the bit is also set in num
                xor_1 ^= num
            else:
                xor_2 ^= num

        return [xor_1, xor_2]


if __name__ == "__main__":
    sol = Solution()

    assert sorted(sol.findSingleNumbers([1, 2, 1, 3, 2, 5])) == [3, 5]

    assert sorted(sol.findSingleNumbers([-1, 0])) == [-1, 0]

    assert sorted(sol.findSingleNumbers([0, 1])) == [0, 1]

    print("All test cases passed.")
