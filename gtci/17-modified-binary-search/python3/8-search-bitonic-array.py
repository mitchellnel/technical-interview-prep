class Solution:
    def search(self, arr, key):
        bitonic_array_max_index = self.find_bitonic_max_index(arr)

        first_half_key_index = self.increasing_binary_search(
            arr, key, 0, bitonic_array_max_index
        )
        if first_half_key_index != -1:
            return first_half_key_index

        return self.decreasing_binary_search(
            arr, key, bitonic_array_max_index, len(arr) - 1
        )

    def find_bitonic_max_index(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

    def increasing_binary_search(self, arr, key, left, right):
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def decreasing_binary_search(self, arr, key, left, right):
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    assert sol.search([1, 3, 8, 4, 3], 4) == 3
    assert sol.search([1, 3, 8, 4, 3], 3) == 1
    assert sol.search([1, 3, 8, 4, 3], 8) == 2
    assert sol.search([10, 20, 30, 40, 50, 40, 30], 30) == 2
    assert sol.search([10, 20, 30, 40, 50, 40, 30], 10) == 0
    assert sol.search([10, 20, 30, 40, 50, 40, 30], 50) == 4
    assert sol.search([10, 20, 30, 40, 50, 40, 30], -1) == -1

    print("All test cases passed.")
