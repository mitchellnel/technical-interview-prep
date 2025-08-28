def get_scheduling_order(tasks, prerequisites):
    if tasks <= 0:
        return []

    topological_ordering = []

    # a. Initialise the graph
    indegrees = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    # b. Build the graph
    for prereq in prerequisites:
        parent, child = prereq[0], prereq[1]

        graph[parent].append(child)
        indegrees[child] += 1

    # c. Look for sources
    queue = []
    for node in indegrees:
        if indegrees[node] == 0:
            queue.append(node)

    # d. BFS to sort -- only add to queue when indegree is 0
    while len(queue) > 0:
        curr_node = queue.pop(0)

        topological_ordering.append(curr_node)

        for child in graph[curr_node]:
            indegrees[child] -= 1

            if indegrees[child] == 0:
                queue.append(child)

    if len(topological_ordering) != tasks:
        return []

    return topological_ordering


def main():
    print("Is scheduling possible: " + str(get_scheduling_order(3, [[0, 1], [1, 2]])))
    print(
        "Is scheduling possible: "
        + str(get_scheduling_order(3, [[0, 1], [1, 2], [2, 0]]))
    )
    print(
        "Is scheduling possible: "
        + str(get_scheduling_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))
    )


main()
