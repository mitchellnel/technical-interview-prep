class Solution:
    def searchTriplets(self, arr, target):
        count = 0

        arr.sort()

        for idx, num in enumerate(arr):
            left = idx + 1
            right = len(arr) - 1

            while left < right:
                current_sum = num + arr[left] + arr[right]

                if current_sum < target:
                    count += right - left
                    left += 1
                elif current_sum >= target:
                    right -= 1

        return count


if __name__ == "__main__":
    sol = Solution()

    assert sol.searchTriplets([-2, 0, 1, 3], 2) == 2
    assert sol.searchTriplets([-1, 4, 2, 1, 3], 5) == 4
    assert sol.searchTriplets([0, 0, 0, 0, 0], 1) == 10
    print("All test cases passed.")
