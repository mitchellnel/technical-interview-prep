class Solution:
    def eventualSafeNodes(self, graph):
        # 0 = visited; 1 = visiting; -1 = safe
        visited = [0] * len(graph)
        safe_nodes = []

        def dfs(curr):
            if visited[curr] == -1:
                return True
            if visited[curr] == 1:  # cycle present
                return False

            visited[curr] = 1
            for node in graph[curr]:
                if not dfs(node):
                    return False

            visited[curr] = -1
            return True

        for i in range(len(graph)):
            if dfs(i):
                safe_nodes.append(i)

        return sorted(safe_nodes)


if __name__ == "__main__":
    sol = Solution()

    assert sol.eventualSafeNodes([[1, 2], [2, 3], [2], [], [5], [6], []]) == [
        3,
        4,
        5,
        6,
    ]
    assert sol.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [], [], [4]]) == [
        2,
        4,
        5,
        6,
    ]
    assert sol.eventualSafeNodes([[1, 2, 3], [2, 3], [3], [], [0, 1, 2]]) == [
        0,
        1,
        2,
        3,
        4,
    ]

    print("All test cases passed.")
