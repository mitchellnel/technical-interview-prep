class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7

        result = 0
        stack = []

        for i in range(len(arr) + 1):
            # sentinel value of 0 at the end -- process remaining stack elements
            curr = 0 if i == len(arr) else arr[i]

            while stack and curr < arr[stack[-1]]:
                min_index = stack.pop()
                previous_index = stack[-1] if stack else -1

                # calculate the number of subarrays for which arr[min_index] is the minimum
                # (min_index - previous_index) is the count of subarrays ending at min_index
                # (i - min_index) is the count of subarrays starting at min_index
                subarray_count = (min_index - previous_index) * (i - min_index)

                result = (result + (arr[min_index] * subarray_count) % MOD) % MOD

            stack.append(i)

        return result


if __name__ == "__main__":
    sol = Solution()

    assert sol.sumSubarrayMins([3, 1, 2, 4]) == 17
    assert sol.sumSubarrayMins([5, 4, 3, 2, 1]) == 35
    assert sol.sumSubarrayMins([3, 1, 2, 4, 5]) == 30
    assert sol.sumSubarrayMins([2, 6, 5, 4]) == 36
    assert sol.sumSubarrayMins([7, 3, 8]) == 27

    print("All test cases passed.")
