def subarraysWithProductLessThanTarget(nums, target):
    result = []

    curr_prod = 1.0

    # our window is nums[left : right + 1]
    left = 0
    for right in range(len(nums)):
        # update the product with the current element
        curr_prod *= nums[right]

        while curr_prod >= target and left < len(nums):
            # slide the left boundary until curr_prod is less than the
            #   target
            curr_prod /= nums[left]
            left += 1

        curr_subarray = []
        for i in range(right, left - 1, -1):
            curr_subarray.insert(0, nums[i])

            result.append(list(curr_subarray))

    return result


def main():
    print(subarraysWithProductLessThanTarget([2, 5, 3, 10], 30))
    print(subarraysWithProductLessThanTarget([8, 2, 6, 5], 50))


main()
