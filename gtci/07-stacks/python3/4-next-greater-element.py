class Solution:
    def nextLargerElement(self, arr):
        res = [-1] * len(arr)

        stack = []

        # iterate through arr in reverse
        for i in range(len(arr) - 1, -1, -1):
            num = arr[i]
            while len(stack) != 0 and stack[-1] <= num:
                stack.pop()

            if len(stack) != 0:
                res[i] = stack[-1]

            stack.append(num)

        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.nextLargerElement([4, 5, 2, 10, 8]) == [5, 10, 10, -1, -1]
    assert sol.nextLargerElement([4, 5, 2, 25]) == [5, 25, 25, -1]
    assert sol.nextLargerElement([13, 7, 6, 12]) == [-1, 12, 12, -1]
    assert sol.nextLargerElement([1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1]
    assert sol.nextLargerElement([3, 2, 1]) == [-1, -1, -1]
    assert sol.nextLargerElement([1, 2, 3]) == [2, 3, -1]

    print("All test cases passed.")
