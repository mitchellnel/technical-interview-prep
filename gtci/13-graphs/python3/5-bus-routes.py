from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        self.construct_stops_to_routes_map(routes)

        visited_routes = set()
        queue = deque()
        for route in self.stops_to_routes[source]:
            queue.append((route, 1))
            visited_routes.add(route)

        while queue:
            curr_route, path_length = queue.popleft()

            visited_routes.add(curr_route)

            if curr_route in self.stops_to_routes[target]:
                return path_length

            for stop in routes[curr_route]:
                for next_route in self.stops_to_routes[stop]:
                    if next_route not in visited_routes:
                        queue.append((next_route, path_length + 1))
                        visited_routes.add(next_route)

        return -1

    def construct_stops_to_routes_map(self, routes):
        # nodes are bus routes, edges are interchanges between routes

        self.stops_to_routes = defaultdict(set)
        for route_id, route in enumerate(routes):
            for stop in route:
                self.stops_to_routes[stop].add(route_id)


if __name__ == "__main__":
    sol = Solution()

    assert sol.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2
    assert (
        sol.numBusesToDestination(
            [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12
        )
        == -1
    )
    assert sol.numBusesToDestination([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 1, 7) == 3
    assert sol.numBusesToDestination([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 1, 8) == -1

    print("All test cases passed.")
