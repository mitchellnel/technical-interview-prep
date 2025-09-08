from collections import deque


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def bfs_traversal(self, start_node):
        visited = set()
        queue = deque([start_node])

        traversal = []

        while queue:
            curr = queue.popleft()

            if curr not in visited:
                traversal.append(curr)
                visited.add(curr)

            for node in self.adjacency_list[curr]:
                if node not in visited:
                    queue.append(node)

        return traversal


if __name__ == "__main__":
    g1 = Graph({0: [1, 2], 1: [0, 3], 2: [0], 3: [1]})
    print(g1.bfs_traversal(0))
    assert g1.bfs_traversal(0) == [0, 1, 2, 3]

    g2 = Graph({0: [1], 1: [0], 2: [3], 3: [2]})
    assert g2.bfs_traversal(0) == [0, 1]
    assert g2.bfs_traversal(2) == [2, 3]

    g3 = Graph({0: []})
    assert g3.bfs_traversal(0) == [0]

    g4 = Graph({0: [1], 1: [2], 2: [0]})
    result = g4.bfs_traversal(0)
    assert set(result) == {0, 1, 2}
    assert result[0] == 0

    # tree-shaped graph
    g5 = Graph({0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []})
    bfs_result_5 = g5.bfs_traversal(0)
    assert bfs_result_5 == [0, 1, 2, 3, 4, 5]

    print("All test cases passed.")
