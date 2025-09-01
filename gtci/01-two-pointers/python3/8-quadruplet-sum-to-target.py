class Solution:
    def searchQuadruplets(self, arr, target):
        if len(arr) < 4:
            return []

        quadruplets = []
        arr.sort()

        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, len(arr)):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                left = j + 1
                right = len(arr) - 1

                while left < right:
                    current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                    if current_sum < target:
                        left += 1
                        while left < right and arr[left] == arr[left - 1]:
                            left += 1
                    elif current_sum > target:
                        right -= 1
                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1
                    else:
                        quadruplets.append([arr[i], arr[j], arr[left], arr[right]])

                        left += 1
                        while left < right and arr[left] == arr[left - 1]:
                            left += 1

                        right -= 1
                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1

        return quadruplets


if __name__ == "__main__":
    sol = Solution()
    assert sol.searchQuadruplets([4, 1, 2, -1, 1, -3], 1) == [
        [-3, -1, 1, 4],
        [-3, 1, 1, 2],
    ]
    assert sol.searchQuadruplets([2, 0, -1, 1, -2, 2], 2) == [
        [-2, 0, 2, 2],
        [-1, 0, 1, 2],
    ]
    assert sol.searchQuadruplets([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
    print("All test cases passed.")
