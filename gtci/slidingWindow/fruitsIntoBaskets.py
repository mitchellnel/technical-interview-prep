def fruits_into_baskets(fruit_trees):
    max_fruits = 0

    fruit_freqs = {}

    window_start = 0
    for window_end in range(len(fruit_trees)):
        # add a fruit to the basket
        fruit = fruit_trees[window_end]
        if fruit not in fruit_freqs:
            fruit_freqs[fruit] = 0
        fruit_freqs[fruit] += 1

        # if we have more than two fruits
        if len(fruit_freqs) > 2:
            # shrink the sliding window until we have only 2 distinct fruits
            leftmost_fruit = fruit_trees[window_start]
            fruit_freqs[leftmost_fruit] -= 1
            if fruit_freqs[leftmost_fruit] == 0:
                del fruit_freqs[leftmost_fruit]
            window_start += 1

        curr_n_fruits = window_end - window_start + 1
        max_fruits = max(max_fruits, curr_n_fruits)

    return max_fruits


def main():
    print(
        "Maximum number of fruits: "
        + str(fruits_into_baskets(["A", "B", "C", "A", "C"]))
    )
    print(
        "Maximum number of fruits: "
        + str(fruits_into_baskets(["A", "B", "C", "B", "B", "C"]))
    )


main()
