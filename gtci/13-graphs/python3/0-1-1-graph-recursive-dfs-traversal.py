class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def dfs_traversal(self, start_node):
        visited = set()

        traversal = []

        self.dfs_traversal_helper(start_node, visited, traversal)

        return traversal

    def dfs_traversal_helper(self, node, visited, traversal):
        if node is None:
            return

        traversal.append(node)
        visited.add(node)

        for vertex in self.adjacency_list[node]:
            if vertex not in visited:
                self.dfs_traversal_helper(vertex, visited, traversal)


if __name__ == "__main__":
    g1 = Graph({0: [1, 2], 1: [0, 3], 2: [0], 3: [1]})
    assert g1.dfs_traversal(0) == [0, 2, 1, 3] or g1.dfs_traversal(0) == [0, 1, 3, 2]

    g2 = Graph({0: [1], 1: [0], 2: [3], 3: [2]})
    assert g2.dfs_traversal(0) == [0, 1]
    assert g2.dfs_traversal(2) == [2, 3]

    g3 = Graph({0: []})
    assert g3.dfs_traversal(0) == [0]

    g4 = Graph({0: [1], 1: [2], 2: [0]})
    result = g4.dfs_traversal(0)
    assert set(result) == {0, 1, 2}
    assert result[0] == 0

    # tree-shaped graph
    g5 = Graph({0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []})
    dfs_result_5 = g5.dfs_traversal(0)
    assert (
        dfs_result_5 == [0, 2, 5, 1, 4, 3]
        or dfs_result_5 == [0, 1, 4, 3, 2, 5]
        or dfs_result_5 == [0, 1, 3, 4, 2, 5]
        or dfs_result_5 == [0, 2, 5, 1, 3, 4]
    )

    print("All test cases passed.")
