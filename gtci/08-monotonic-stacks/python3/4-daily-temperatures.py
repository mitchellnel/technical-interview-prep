class Solution:
    def dailyTemperatures(self, temperatures):
        days_to_wait = [0 for temp in temperatures]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                stack_temp_idx = stack.pop()

                days_to_wait[stack_temp_idx] = i - stack_temp_idx

            stack.append(i)

        return days_to_wait


if __name__ == "__main__":
    sol = Solution()

    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]
    assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert sol.dailyTemperatures([30, 60, 90]) == [1, 1, 0]

    print("All test cases passed.")
