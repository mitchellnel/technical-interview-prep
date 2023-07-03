def find_two_single_numbers(array):
    # get xor of all numbers in array
    num1_xor_num2 = array[0]
    for i in range(1, len(array)):
        num1_xor_num2 ^= array[i]

    # find the rightmost set bit
    rightmost_set_bit = 1
    while rightmost_set_bit & num1_xor_num2 == 0:
        rightmost_set_bit = rightmost_set_bit << 1

    num1 = 0
    num2 = 0

    for num in array:
        # the bit is set
        if rightmost_set_bit & num != 0:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]


def main():
    print(
        "Single numbers are:"
        + str(find_two_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
    )
    print("Single numbers are:" + str(find_two_single_numbers([2, 1, 3, 2])))


main()
