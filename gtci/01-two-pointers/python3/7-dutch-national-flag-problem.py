class Solution:
    def sort(self, arr):
        low = 0  # where the 0s will go
        high = len(arr) - 1  # where the 2s will go

        idx = 0
        while idx <= high:
            if arr[idx] == 0:
                arr[idx], arr[low] = arr[low], arr[idx]
                low += 1
                idx += 1
            elif arr[idx] == 1:  # 1s stay in the middle
                idx += 1
            else:
                arr[idx], arr[high] = arr[high], arr[idx]
                high -= 1

        return arr


if __name__ == "__main__":
    sol = Solution()

    assert sol.sort([0, 1, 2, 0, 1, 2]) == [0, 0, 1, 1, 2, 2]
    assert sol.sort([2, 2, 0, 1, 2, 0]) == [0, 0, 1, 2, 2, 2]
    print("All test cases passed.")
