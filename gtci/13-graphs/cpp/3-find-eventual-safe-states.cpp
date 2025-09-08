#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        vector<int> safeNodes;
        vector<int> visited (graph.size(), 0);
        
        for (int i = 0; i < graph.size(); i++) {
            if (dfs(i, visited, graph))
                safeNodes.push_back(i);
        }

        std::sort(safeNodes.begin(), safeNodes.end());
        return safeNodes;
    }

private:
    bool dfs(const int& curr, std::vector<int>& visited, const vector<vector<int>>& graph) {
        if (visited[curr] == -1)
            return true;
        if (visited[curr] == 1)     // cycle present
            return false;

        visited[curr] = 1;
        for (const int node : graph[curr]) {
            if (!dfs(node, visited, graph)) {
                return false;
            }
        }

        visited[curr] = -1;
        return true;
    }
};

int main() {
    Solution s;

    vector<vector<int>> graph1 = {{1, 2}, {2, 3}, {2}, {}, {5}, {6}, {}};
    assert(s.eventualSafeNodes(graph1) == vector<int>({3, 4, 5, 6}));

    vector<vector<int>> graph2 = {{1, 2}, {2, 3}, {5}, {0}, {}, {}, {4}};
    assert(s.eventualSafeNodes(graph2) == vector<int>({2, 4, 5, 6}));

    vector<vector<int>> graph3 = {{1, 2, 3}, {2, 3}, {3}, {}, {0, 1, 2}};
    assert(s.eventualSafeNodes(graph3) == vector<int>({0, 1, 2, 3, 4}));

    cout << "All test cases passed." << endl;

    return 0;
}
