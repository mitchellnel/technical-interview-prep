def find_binary_complement(num):
    # get number of bits we need
    n_bits = 0
    n = num
    while n > 0:
        n_bits += 1
        n = n >> 1

    # get a number with all the bits set
    # this will be 2^n_bits - 1
    #   (2^n_bits - 1 == 1000....0 - 000...1 == 111...1)
    all_bits_set = 2**n_bits - 1

    # num ^ all_bits_set == complement
    return num ^ all_bits_set


def main():
    print("Bitwise complement is: " + str(find_binary_complement(8)))
    print("Bitwise complement is: " + str(find_binary_complement(10)))


main()
