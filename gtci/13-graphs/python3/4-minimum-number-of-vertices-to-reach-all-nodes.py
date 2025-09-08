from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n

        for start, end in edges:
            indegrees[end] += 1

        return [node for node in range(n) if indegrees[node] == 0]


if __name__ == "__main__":
    sol = Solution()

    assert sol.findSmallestSetOfVertices(
        6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    ) == [0, 3]
    assert sol.findSmallestSetOfVertices(3, [[0, 1], [2, 1]]) == [0, 2]
    assert sol.findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 4]]) == [0, 2, 3]

    print("All test cases passed.")
