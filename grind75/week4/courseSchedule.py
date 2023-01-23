from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialise the graph
        indegrees = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        # build the graph
        for prereq in prerequisites:
            sink = prereq[0]
            source = prereq[1]

            graph[source].append(sink)
            indegrees[sink] += 1

        # find all sources
        queue = []
        for node in indegrees:
            if indegrees[node] == 0:
                queue.append(node)

        # topological sort using BFS
        topological_order = []
        while len(queue) > 0:
            curr_node = queue.pop(0)

            topological_order.append(curr_node)

            for child in graph[curr_node]:
                indegrees[child] -= 1

                if indegrees[child] == 0:
                    queue.append(child)

        return len(topological_order) == numCourses


def main():
    soln = Solution()

    print(f"numCourses = 2, prerequisites = [[1,0]] --> {soln.canFinish(2, [[1,0]])}")
    print(
        f"numCourses = 2, prerequisites = [[1,0],[0,1]] --> {soln.canFinish(2, [[1,0],[0,1]])}"
    )


main()
