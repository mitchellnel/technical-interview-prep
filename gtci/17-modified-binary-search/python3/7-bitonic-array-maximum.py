class Solution:
    def findMax(self, arr):
        if not arr:
            return -1

        left = 0
        right = len(arr) - 1

        # instead of comparing against target, we will work out
        # whether we are in the increasing half or the decreasing half
        while left < right:
            mid = (left + right) // 2

            if mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                # increasing half, so converge towards the peak
                left = mid + 1
            else:
                # decreasing half, so converge backwards to the peak
                right = mid

        return arr[left]


if __name__ == "__main__":
    sol = Solution()

    assert sol.findMax([1, 3, 8, 4, 3]) == 8
    assert sol.findMax([10, 20, 30, 40, 50]) == 50
    assert sol.findMax([120, 100, 80, 20, 0]) == 120
    assert sol.findMax([]) == -1

    print("All test cases passed.")
