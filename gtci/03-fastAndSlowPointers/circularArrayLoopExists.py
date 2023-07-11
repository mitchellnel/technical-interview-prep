def findNextIndex(arr, is_forward, curr_idx):
    direction = arr[curr_idx] >= 0

    if is_forward != direction:
        # change in direction, so return -1 -- no cycle here
        return -1

    next_idx = (curr_idx + arr[curr_idx]) % len(arr)

    if next_idx == curr_idx:
        # one element cycle, so return -1 -- invalid cycle
        return -1

    return next_idx


def circularArrayLoopExists(arr):
    for i in range(len(arr)):
        # are we moving forward or backward?
        is_forward = arr[i] >= 0

        slow, fast = i, i

        # if slow or fast become -1, this means we cannot find a cycle for
        #   this number
        while True:
            # move one step for slow pointer
            slow = findNextIndex(arr, is_forward, slow)

            # move two steps for fast pointer
            fast = findNextIndex(arr, is_forward, fast)
            if fast != -1:
                # move another step only if we are able to continue looking
                #   for a cycle
                fast = findNextIndex(arr, is_forward, fast)

            # check break conditions
            if slow == -1 or fast == -1:
                # could not find cycle
                break
            elif slow == fast:
                # found cycle
                break

    return slow != -1 and slow == fast


def circularArrayLoopExists_faster(arr):
    visited = set()

    for i in range(len(arr)):
        curr_path = set()

        # are we moving forward or backward?
        is_forward = arr[i] >= 0

        slow, fast = i, i

        # if slow or fast become -1, this means we cannot find a cycle for
        #   this number
        while True:
            # move one step for slow pointer
            slow = findNextIndex(arr, is_forward, slow)

            # move two steps for fast pointer
            fast = findNextIndex(arr, is_forward, fast)
            if fast != -1:
                # move another step only if we are able to continue looking
                #   for a cycle
                fast = findNextIndex(arr, is_forward, fast)

            # check break conditions
            if slow in visited or fast in visited:
                # already checked these indexes for cycles
                break
            elif slow == -1 or fast == -1:
                # could not find cycle
                visited.update(curr_path)
                break
            elif slow == fast:
                # found cycle
                break

            curr_path.add(slow)
            curr_path.add(fast)

    return slow != -1 and slow == fast


def main():
    print(circularArrayLoopExists([1, 2, -1, 2, 2]))
    print(circularArrayLoopExists([2, 2, -1, 2]))
    print(circularArrayLoopExists([2, 1, -1, -2]))


main()
