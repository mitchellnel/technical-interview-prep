import math


class Solution:
    def searchTriplet(self, arr, target_sum):
        closest_sum = None
        closest_distance = None

        arr.sort()

        for idx, num in enumerate(arr):
            if idx > 0 and num == arr[idx - 1]:
                continue

            left = idx + 1
            right = len(arr) - 1

            while left < right:
                current_sum = num + arr[left] + arr[right]
                current_distance = abs(target_sum - current_sum)

                if current_sum == target_sum:
                    return current_sum

                if closest_sum is None:
                    closest_sum = current_sum
                    closest_distance = current_distance
                elif current_distance < closest_distance or (
                    current_distance <= closest_distance and current_sum < closest_sum
                ):
                    closest_sum = current_sum
                    closest_distance = current_distance

                if current_sum < target_sum:
                    left += 1
                elif current_sum > target_sum:
                    right -= 1

        return closest_sum


if __name__ == "__main__":
    sol = Solution()
    arr = [-2, -1, 0, 1, 2]
    target_sum = 0
    assert sol.searchTriplet(arr, target_sum) == 0

    arr2 = [-3, -1, 1, 2]
    target_sum2 = 1
    assert sol.searchTriplet(arr2, target_sum2) == 0

    arr3 = [1, 0, 1, 1]
    target_sum3 = 100
    assert sol.searchTriplet(arr3, target_sum3) == 3

    print("All test cases passed.")
