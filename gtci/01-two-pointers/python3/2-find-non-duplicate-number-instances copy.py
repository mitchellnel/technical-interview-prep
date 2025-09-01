class Solution:
    def moveElements(self, arr):
        next_non_duplicate = 1

        for i in range(1, len(arr)):
            if arr[i] != arr[next_non_duplicate - 1]:
                arr[next_non_duplicate] = arr[i]

                next_non_duplicate += 1

        return next_non_duplicate


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 3, 3, 6, 6, 7, 8, 9, 9]
    new_length = sol.moveElements(arr)
    assert arr[:new_length] == [2, 3, 6, 7, 8, 9]

    arr2 = [2, 2, 2, 11]
    new_length = sol.moveElements(arr2)
    assert arr2[:new_length] == [2, 11]
    print("All test cases passed.")
