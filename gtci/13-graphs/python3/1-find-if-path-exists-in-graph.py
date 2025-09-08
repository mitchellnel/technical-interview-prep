class Solution:
    def validPath(self, n: int, edges: [[int]], start: int, end: int) -> bool:
        adjacency_list = self.construct_adjacency_list(n, edges)

        visited = set()
        stack = [start]

        while stack:
            curr = stack.pop()

            if curr == end:
                return True

            visited.add(curr)

            for node in adjacency_list[curr]:
                if node not in visited:
                    stack.append(node)

        return False

    def construct_adjacency_list(self, n: int, edges: [[int]]) -> {int: [int]}:
        adjacency_list = {v: [] for v in range(n)}

        for edge in edges:
            start, end = edge

            adjacency_list[start].append(end)
            adjacency_list[end].append(start)

        return adjacency_list


if __name__ == "__main__":
    s = Solution()

    assert s.validPath(4, [[0, 1], [1, 2], [2, 3]], 0, 3)
    assert not s.validPath(4, [[0, 1], [2, 3]], 0, 3)
    assert not s.validPath(5, [[0, 1], [3, 4]], 0, 4)
    assert s.validPath(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 0, 4)

    print("All test cases passed.")
