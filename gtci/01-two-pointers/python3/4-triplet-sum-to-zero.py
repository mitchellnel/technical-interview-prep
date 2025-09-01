class Solution:
    def searchTriplets(self, arr):
        triplets = []

        arr.sort()

        for idx, num in enumerate(arr):
            if idx > 0 and num == arr[idx - 1]:
                continue

            left = idx + 1
            right = len(arr) - 1

            while left < right:
                total_sum = num + arr[left] + arr[right]

                if total_sum < 0:
                    left += 1

                elif total_sum > 0:
                    right -= 1
                else:
                    triplets.append([num, arr[left], arr[right]])

                    left += 1
                    while left < right and arr[left - 1] == arr[left]:
                        left += 1

                    right -= 1
                    while left < right and arr[right + 1] == arr[right]:
                        right -= 1

        return triplets


if __name__ == "__main__":
    sol = Solution()

    arr = [-2, -1, 0, 1, 2]
    result = sol.searchTriplets(arr)
    assert sorted(result) == sorted([[-2, 0, 2], [-1, 0, 1]])

    arr2 = [-1, 0, 1, 2, -1, -4]
    result2 = sol.searchTriplets(arr2)
    assert sorted(result2) == sorted([[-1, -1, 2], [-1, 0, 1]])

    arr3 = [-3, -2, -1]
    result3 = sol.searchTriplets(arr3)
    assert sorted(result3) == sorted([])

    print("All test cases passed.")
