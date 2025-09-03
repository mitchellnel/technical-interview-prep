class Solution:
    # this solves in O(n) time, O(1) space, but does not modify the input array
    def findNumber(self, nums):
        # find whether there's a cycle
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    sol = Solution()

    assert sol.findNumber([1, 4, 4, 3, 2]) == 4
    assert sol.findNumber([2, 1, 3, 3, 5, 4]) == 3
    assert sol.findNumber([2, 4, 1, 4, 4]) == 4

    print("All test cases passed.")
