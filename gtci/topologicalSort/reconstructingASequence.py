def can_reconstruct_sequence(original, seqs):
    if len(original) == 0:
        return True

    reconstructed_sequence = []

    # a. Initialise the graph
    indegrees = {}
    graph = {}

    for seq in seqs:
        for num in seq:
            indegrees[num] = 0
            graph[num] = []

    # b. Build the graph
    for seq in seqs:
        for i in range(1, len(seq)):
            parent, child = seq[i - 1], seq[i]

            graph[parent].append(child)
            indegrees[child] += 1

    # if we do not have ordering rules for all the numbers, we'll not be able to uniquely construct
    #   the sequence
    if len(indegrees) != len(original):
        return False

    # c. Find the sources
    queue = []

    # we want to have the sources ordered such that they match the order they occur in the
    #   original sequence -- this is to ensure we get the right topological order
    for node in indegrees:
        if indegrees[node] == 0:
            queue.append(node)

    # d. Topologically sort
    while len(queue) > 0:
        # more than one source at any time means that there is more than one way to reconstruct
        #   the sequence
        if len(queue) > 1:
            return False

        # if the next source is different from the original sequence, we can't reconstruct the
        #   sequence
        if original[len(reconstructed_sequence)] != queue[0]:
            return False

        curr_node = queue.pop(0)

        reconstructed_sequence.append(curr_node)

        for child in graph[curr_node]:
            indegrees[child] -= 1

            if indegrees[child] == 0:
                queue.append(child)

    return len(original) == len(reconstructed_sequence)


def main():
    print(
        "Can construct: "
        + str(can_reconstruct_sequence([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]]))
    )
    print(
        "Can construct: "
        + str(can_reconstruct_sequence([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]]))
    )
    print(
        "Can construct: "
        + str(can_reconstruct_sequence([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]]))
    )


main()
