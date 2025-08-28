def tripletWithSmallerSum(arr, target):
    count = 0

    arr.sort()

    for i in range(len(arr)):
        count += findPair(arr, arr[i], i + 1, target)

    return count


def findPair(arr, curr, left, target):
    count = 0

    right = len(arr) - 1
    while left < right:
        current_sum = curr + arr[left] + arr[right]

        if current_sum < target:
            # since arr[right] >= arr[left], we can include all the triplets
            #   formed by numbers downstream of right
            count += right - left

            # consider triplets with a larger sum
            left += 1
        else:
            # we need a triplet with a smaller sum
            right -= 1

    return count


def tripletWithSmallerSum_obtainTriplets(arr, target):
    triplets = []

    arr.sort()

    for i in range(len(arr)):
        findPair_obtainTriplets(arr, arr[i], i + 1, target, triplets)

    return triplets


def findPair_obtainTriplets(arr, curr, left, target, triplets):
    right = len(arr) - 1
    while left < right:
        current_sum = curr + arr[left] + arr[right]

        if current_sum < target:
            # since arr[right] >= arr[left], we can include all the triplets
            #   formed by numbers downstream of right
            for i in range(right, left, -1):
                triplets.append([curr, arr[left], arr[i]])

            # consider triplets with a larger sum
            left += 1
        else:
            # we need a triplet with a smaller sum
            right -= 1


def main():
    print(tripletWithSmallerSum_obtainTriplets([-1, 0, 2, 3], 3))
    print(tripletWithSmallerSum_obtainTriplets([-1, 4, 2, 1, 3], 5))


main()
