def squareSortedArray_1(nums):
    squares = []

    non_neg = 0
    while non_neg < len(nums) and nums[non_neg] < 0:
        non_neg += 1

    if non_neg == len(nums):
        neg = len(nums) - 1
    else:
        neg = non_neg - 1

    while neg >= 0 or non_neg < len(nums):
        if neg >= 0 and non_neg < len(nums):
            neg_square = nums[neg] ** 2
            non_neg_square = nums[non_neg] ** 2

            if neg_square < non_neg_square:
                squares.append(neg_square)

                neg -= 1
            elif non_neg_square < neg_square:
                squares.append(non_neg_square)

                non_neg += 1
            else:
                squares.append(neg_square)
                squares.append(non_neg_square)

                neg -= 1
                non_neg += 1
        elif neg >= 0:
            squares.append(nums[neg] ** 2)

            neg -= 1
        else:
            squares.append(nums[non_neg] ** 2)

            non_neg += 1

    return squares


def squareSortedArray_2(nums):
    squares = [0 for _ in range(len(nums))]

    highest_square_idx = len(nums) - 1

    left, right = 0, len(nums) - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            squares[highest_square_idx] = left_square

            left += 1
        elif right_square > left_square:
            squares[highest_square_idx] = right_square

            right -= 1
        else:
            squares[highest_square_idx] = left_square
            highest_square_idx -= 1
            squares[highest_square_idx] = right_square

            left += 1
            right -= 1

        highest_square_idx -= 1

    return squares


def main():

    print("Squares: " + str(squareSortedArray_1([-2, -1, 0, 2, 3])))
    print("Squares: " + str(squareSortedArray_1([-3, -1, 0, 1, 2])))


main()
