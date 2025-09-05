class Solution:
    def nextGreaterElement(self, nums1, nums2):
        next_greater_element = {}
        stack = []

        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) > 0 and nums2[i] > stack[-1]:
                stack.pop()

            next_greater_element[nums2[i]] = stack[-1] if len(stack) > 0 else -1
            stack.append(nums2[i])

        return [next_greater_element.get(num, -1) for num in nums1]


if __name__ == "__main__":
    sol = Solution()

    assert sol.nextGreaterElement([4, 2, 6], [6, 2, 4, 5, 3, 7]) == [5, 4, 7]
    assert sol.nextGreaterElement([9, 7, 1], [1, 7, 9, 5, 4, 3]) == [-1, 9, 7]
    assert sol.nextGreaterElement([5, 12, 3], [12, 3, 5, 4, 10, 15]) == [10, 15, 5]

    print("All test cases passed.")
