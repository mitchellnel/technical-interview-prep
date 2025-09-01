class Solution:
    def findSubarrays(self, nums, target):
        if target < 1:
            return 0

        total_count = 0

        window_start = 0
        window_product = 1
        for window_end in range(len(nums)):
            window_product *= nums[window_end]

            while window_start < len(nums) and window_product >= target:
                window_product //= nums[window_start]

                window_start += 1

            if window_product < target:
                total_count += window_end - window_start + 1

        return total_count


if __name__ == "__main__":
    sol = Solution()
    assert sol.findSubarrays([2, 5, 3, 10], 30) == 6
    assert sol.findSubarrays([8, 2, 6, 5], 50) == 7
    assert sol.findSubarrays([10, 5, 2, 6], 0) == 0
    assert sol.findSubarrays([2], 1) == 0
    print("All test cases passed.")
