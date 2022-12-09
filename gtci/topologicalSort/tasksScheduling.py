def is_scheduling_possible(tasks, prerequisites):
    if tasks <= 0:
        return True

    topological_order = []

    # a. Initialise the graph
    indegrees = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    # b. Build the graph
    for prereq in prerequisites:
        parent, child = prereq[0], prereq[1]

        graph[parent].append(child)
        indegrees[child] += 1

    # c. Find all sources, i.e. all vertices with indegree 0
    queue = []
    for node in indegrees:
        if indegrees[node] == 0:
            queue.append(node)

    # d. For each source, add it to the topological ordering and subtract 1 from all of its
    #       childrens indegrees; if a child's indegree becomes zero, add it to the sources queue
    while len(queue) > 0:
        curr_node = queue.pop(0)

        topological_order.append(curr_node)

        for child in graph[curr_node]:
            indegrees[child] -= 1

            if indegrees[child] == 0:
                queue.append(child)

    return len(topological_order) == tasks


def main():
    print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print(
        "Is scheduling possible: "
        + str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]]))
    )
    print(
        "Is scheduling possible: "
        + str(
            is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
        )
    )


main()
