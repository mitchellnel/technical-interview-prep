import heapq


class Solution:
    def findMaximumCapital(self, capital, profits, numberOfProjects, initialCapital):
        self.max_heap = (
            []
        )  # max heap on profits -- all the projects we can afford are in the heap

        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        capital, profits = zip(*projects)

        n_projects_chosen = 0
        capital_available = initialCapital
        next_project_to_consider = 0
        while n_projects_chosen < numberOfProjects:
            # put all the projects we can afford into the heap
            next_project_to_consider = self.populate_heap(
                next_project_to_consider, capital, profits, capital_available
            )

            # choose the most profitable project we can afford
            if not self.max_heap:
                break

            profit, project = heapq.heappop(self.max_heap)
            profit = -profit

            capital_available += profit
            n_projects_chosen += 1

        return capital_available

    def populate_heap(
        self, next_project_to_consider, capital, profits, capital_available
    ):
        project = next_project_to_consider
        while project < len(capital) and capital[project] <= capital_available:
            heapq.heappush(self.max_heap, (-profits[project], project))
            project += 1

        return project


if __name__ == "__main__":
    solution = Solution()

    capital = [0, 1, 2]
    profits = [1, 2, 3]
    numberOfProjects = 2
    initialCapital = 1
    assert (
        solution.findMaximumCapital(capital, profits, numberOfProjects, initialCapital)
        == 6
    )

    capital = [0, 1, 2, 3]
    profits = [1, 2, 3, 5]
    numberOfProjects = 3
    initialCapital = 0
    assert (
        solution.findMaximumCapital(capital, profits, numberOfProjects, initialCapital)
        == 8
    )

    print("All test cases passed.")
