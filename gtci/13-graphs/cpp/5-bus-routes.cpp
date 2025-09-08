#include <cassert>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    std::unordered_map<int, std::unordered_set<int>> stopsToRoutes;
    
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        constructStopsToRoutesMap(routes);

        std::unordered_set<int> visitedRoutes;
        std::queue<std::pair<int, int>> queue;
        
        for (auto route : stopsToRoutes[source]) {
            queue.push({route, 1});
            visitedRoutes.insert(route);
        }

        while (!queue.empty()) {
            auto [curr_route, pathLength] = queue.front();
            queue.pop();

            if (routes[curr_route].end() != std::find(routes[curr_route].begin(), routes[curr_route].end(), target)) {
                return pathLength;
            }
            
            for (auto stop : routes[curr_route]) {
                for (auto nextRoute : stopsToRoutes[stop]) {
                    if (!visitedRoutes.contains(nextRoute)) {
                        queue.push({nextRoute, pathLength + 1});
                        visitedRoutes.insert(nextRoute);
                    }
                }
            }
        }

        return -1;
    }
private:
    void constructStopsToRoutesMap(const std::vector<std::vector<int>>& routes) {
        for (int routeId = 0; routeId < routes.size(); routeId++) {
            const auto& route = routes[routeId];

            for (auto stop : route) {
                stopsToRoutes[stop].insert(routeId);
            }
        }
    }
};

int main() {
    Solution sol;
    auto routes1 = vector<vector<int>>{{1, 2, 7}, {3, 6, 7}};
    assert(sol.numBusesToDestination(routes1, 1, 6) == 2);

    sol = Solution();
    auto routes2 = vector<vector<int>>{{7, 12}, {4, 5, 15}, {6}, {15, 19}, {9, 12, 13}};
    assert(sol.numBusesToDestination(routes2, 15, 12) == -1);

    sol = Solution();
    auto routes3 = vector<vector<int>>{{1, 2, 3}, {3, 4, 5}, {5, 6, 7}};
    assert(sol.numBusesToDestination(routes3, 1, 7) == 3);

    sol = Solution();
    auto routes4 = vector<vector<int>>{{1, 2, 3}, {3, 4, 5}, {5, 6, 7}};
    assert(sol.numBusesToDestination(routes4, 1, 8) == -1);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
