def intervalIntersection(intervals_a, intervals_b):
    intersection = []

    START, END = 0, 1

    i, j = 0, 0
    while i < len(intervals_a) and j < len(intervals_b):
        a, b = intervals_a[i], intervals_b[j]

        # check if the intervals overlap, and a's start time lies within b
        a_overlaps_b = b[START] <= a[END] and a[START] <= b[END]

        # check if the intervals overlap, and b's start time lies within a
        b_overlaps_a = a[START] <= b[END] and b[START] <= a[END]

        # store the intersecting part
        if a_overlaps_b or b_overlaps_a:
            overlap_start = max(a[START], b[START])
            overlap_end = min(a[END], b[END])

            intersection.append([overlap_start, overlap_end])

        # move next from the interval that finishes first
        if a[END] < b[END]:
            i += 1
        else:
            j += 1

    return intersection


def main():
    print(
        "Intervals Intersection: "
        + str(intervalIntersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
    )
    print(
        "Intervals Intersection: "
        + str(intervalIntersection([[1, 3], [5, 7], [9, 12]], [[5, 10]]))
    )


main()
