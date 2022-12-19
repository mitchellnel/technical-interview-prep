def can_partition(nums):
    n = len(nums)
    s = sum(nums)

    # if s is odd, we can't have two subsets with equal sum
    if s % 2 != 0:
        return False

    s = int(s / 2)

    dp = [[False for _ in range(int(s + 1))] for _ in range(len(nums))]

    # populate the s=0 columns, as we can always form a 0 sum with an empty set
    for i in range(0, n):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is equal to its value
    for j in range(1, s + 1):
        dp[0][j] = nums[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, s + 1):
            # if we can get the sum j without the number at index i
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                # else if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - nums[i]]

    # bottom-right corner has our answer
    return dp[n - 1][s]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
