def find_string_permutations_by_changing_case(string):
    permutations = [string]

    # process every character of the string one-by-one
    for idx, char in enumerate(string):
        if char.isalpha():  # only process chars, skip digits
            # we will take all existing permutations and change the letter
            #   case appropriately
            n = len(permutations)
            for j in range(n):
                old_permutation = permutations[j]

                new_permutation = list(old_permutation)
                new_permutation[idx] = new_permutation[idx].swapcase()

                permutations.append("".join(new_permutation))

    return permutations


def main():
    print(
        "String permutations are: "
        + str(find_string_permutations_by_changing_case("ad52"))
    )
    print(
        "String permutations are: "
        + str(find_string_permutations_by_changing_case("ab7c"))
    )


main()
