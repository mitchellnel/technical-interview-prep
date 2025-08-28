def topological_sort(vertices, edges):
    if vertices <= 0:
        return []

    topological_order = []

    # a. Initialise the graph
    indegrees = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph

    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]

        graph[parent].append(child)  # put child into it's parent's list
        indegrees[child] += 1  # increment child indegree

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

    # topological sort is not possible as the graph has a cycle
    if len(topological_order) != vertices:
        return []

    return topological_order


def main():
    print(
        "Topological sort: "
        + str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
    )
    print(
        "Topological sort: "
        + str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
    )
    print(
        "Topological sort: "
        + str(
            topological_sort(
                7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
            )
        )
    )


main()
