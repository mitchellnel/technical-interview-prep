def search(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while left < right:
        candidate_sum = arr[left] + arr[right]

        if candidate_sum < target_sum:
            left += 1
        elif candidate_sum > target_sum:
            right -= 1
        else:
            return [left, right]

    return [-1, -1]


if __name__ == "__main__":
    assert search([1, 2, 3, 4, 6], 6) == [1, 3]
    assert search([2, 5, 9, 11], 11) == [0, 2]
    assert search([1, 3, 5, 7], 8) == [0, 3]
    assert search([1, 2, 3, 4, 5], 10) == [-1, -1]
    print("All test cases passed.")
