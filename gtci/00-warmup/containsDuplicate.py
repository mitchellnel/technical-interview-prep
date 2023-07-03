def containsDuplicate(nums):
    appears = {}

    for num in nums:
        if num in appears:
            return True

        appears[num] = True

    return False


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4]
    print(containsDuplicate(nums1))  # Expected output: False

    nums2 = [1, 2, 3, 1]
    print(containsDuplicate(nums2))  # Expected output: True

    nums3 = []
    print(containsDuplicate(nums3))  # Expected output: False

    nums4 = [1, 1, 1, 1]
    print(containsDuplicate(nums4))  # Expected output: True
