def contains_duplicate(nums: list[int]) -> bool:
    counts = {}

    for num in nums:
        if num not in counts:
            counts[num] = 0
        else:
            return True

    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))  # True
    print(contains_duplicate([1, 2, 3, 4]))  # False
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
