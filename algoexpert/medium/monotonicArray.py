# O(n) time | O(1) space
def isMonotonic_logical_ops(array):
    if len(array) <= 2:
        return True

    increasing = False
    decreasing = False

    for idx, num in enumerate(array):
        if idx == len(array) - 1:
            break

        if array[idx] < array[idx + 1]:
            increasing = True
        elif array[idx] > array[idx + 1]:
            decreasing = True

    return (
        True
        if increasing is False
        and decreasing is True
        or increasing is True
        and decreasing is False
        or increasing is False
        and decreasing is False
        else False
    )


# O(n) time | O(1) space
def isMonotonic(array):
    if len(array) <= 2:
        return True

    # check for initial direction
    direction = array[1] - array[0]

    for i in range(2, len(array)):
        # if direction is 0, we haven't found an increasing or dcreasing num yet
        if direction == 0:
            # so try and find a increasing or decreasing direction
            direction = array[i] - array[i - 1]
            continue

        if breaksDirection(direction, array[i - 1], array[i]):
            return False

    return True


def breaksDirection(direction, prev, curr):
    # use the diff between prev and curr to check for directional breakage
    diff = curr - prev
    if direction > 0:
        return diff < 0
    else:
        return diff > 0
