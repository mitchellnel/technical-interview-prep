def find_MHT_roots(nodes, edges):
    if nodes <= 0:
        return []

    # with only one node, its indegrees will be 0, so handle it separately
    if nodes == 1:
        return [0]

    # a. Initialise the graph
    indegrees = {i: 0 for i in range(nodes)}
    graph = {i: [] for i in range(nodes)}

    # b. Build the graph
    for edge in edges:
        n1, n2 = edge[0], edge[1]

        # this is an undirected graph, so add a link for both nodes
        graph[n1].append(n2)
        graph[n2].append(n1)

        indegrees[n1] += 1
        indegrees[n2] += 1

    # c. Find the leaves
    leaves = []
    for node in indegrees:
        if indegrees[node] == 1:
            leaves.append(node)

    # d. Modified Topological Sort
    # remove leaves level-by-level and subtract each leave's children's indegrees
    # repeat this until we are left with 1 or 2 nodes, which will be our answer
    # any node that has already been a leaf cannot be an MHT root
    total_nodes = nodes
    while total_nodes > 2:
        n_leaves = len(leaves)

        total_nodes -= n_leaves

        for i in range(0, n_leaves):
            leaf = leaves.pop(0)

            # get the leaf's children to decrement their indegrees
            for child in graph[leaf]:
                indegrees[child] -= 1

                if indegrees[child] == 1:
                    leaves.append(child)

        print(indegrees)

    return list(leaves)


def main():
    print("Roots of MHTs: " + str(find_MHT_roots(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " + str(find_MHT_roots(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " + str(find_MHT_roots(4, [[1, 2], [1, 3]])))


main()
