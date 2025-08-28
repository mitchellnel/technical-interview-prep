def removeDuplicates_counting(arr):
    if not arr:
        return 0

    unique_count = 1
    unique, next_unique = 0, 1

    while next_unique != len(arr):
        if arr[unique] == arr[next_unique]:
            next_unique += 1
        else:
            unique_count += 1
            unique = next_unique
            next_unique += 1

    return unique_count


def removeDuplicates(arr):
    if not arr:
        return 0

    curr, next_non_duplicate = 0, 1

    while curr != len(arr):
        if arr[next_non_duplicate] != arr[curr]:
            arr[next_non_duplicate] = arr[curr]
            next_non_duplicate += 1

        curr += 1

    return next_non_duplicate


def main():
    print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
    print(removeDuplicates([2, 2, 2, 11]))


main()
