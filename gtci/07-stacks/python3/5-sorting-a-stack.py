class Solution:
    def sortStack(self, stack):
        if len(stack) < 2:
            return stack

        sorted_stack = []

        while len(stack) > 0:
            top = stack.pop()

            while len(sorted_stack) > 0 and sorted_stack[-1] > top:
                stack.append(sorted_stack.pop())

            sorted_stack.append(top)

        return sorted_stack


if __name__ == "__main__":
    sol = Solution()

    assert sol.sortStack([34, 3, 31, 98, 92, 23]) == [3, 23, 31, 34, 92, 98]
    assert sol.sortStack([4, 3, 2, 10, 12, 1, 5, 6]) == [1, 2, 3, 4, 5, 6, 10, 12]
    assert sol.sortStack([20, 10, -5, -1]) == [-5, -1, 10, 20]

    print("All test cases passed.")
