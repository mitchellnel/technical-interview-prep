class Solution:
    def remove_target_key(self, arr, key):
        next_non_key = 0

        for i in range(0, len(arr)):
            if arr[i] != key:
                arr[next_non_key] = arr[i]
                next_non_key += 1

        return next_non_key


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 3, 3, 6, 6, 7, 8, 9, 9]
    new_length = sol.remove_target_key(arr, 3)
    assert arr[:new_length] == [2, 6, 6, 7, 8, 9, 9]

    arr2 = [2, 2, 2, 11]
    new_length = sol.remove_target_key(arr2, 2)
    assert arr2[:new_length] == [11]
    print("All test cases passed.")
