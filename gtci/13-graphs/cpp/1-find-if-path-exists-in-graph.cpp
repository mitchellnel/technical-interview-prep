#include <cassert>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int start, int end) {
        std::unordered_map<int, std::vector<int>> adjacencyList = constructAdjacencyList(n, edges);

        std::unordered_set<int> visited;
        std::stack<int> stack;
        stack.push(start);

        while (!stack.empty()) {
            const int curr = stack.top();
            stack.pop();

            if (curr == end)
                return true;
            
            visited.insert(curr);

            for (auto node : adjacencyList[curr]) {
                if (!visited.contains(node))
                    stack.push(node);
            }
        }

        return false;
    }

    std::unordered_map<int, std::vector<int>> constructAdjacencyList(
        const int& n,
        const vector<vector<int>>& edges
    ) {
        std::unordered_map<int, std::vector<int>> adjacencyList;

        for (auto edge : edges) {
            const int start = edge[0];
            const int end = edge[1];

            adjacencyList[start].push_back(end);
            adjacencyList[end].push_back(start);
        }

        return adjacencyList;
    }
};

int main() {
    Solution sol;

    vector<vector<int>> edges1 = {{0,1},{0,2},{3,5},{5,4},{4,3}};
    assert(sol.validPath(6, edges1, 0, 5) == false);

    vector<vector<int>> edges2 = {{0,1},{0,2},{2,5},{3,5},{5,4},{4,3}};
    assert(sol.validPath(6, edges2, 0, 5) == true);

    vector<vector<int>> edges3 = {{0,1}};
    assert(sol.validPath(3, edges3, 0, 2) == false);

    vector<vector<int>> edges4 = {{0,1},{1,2},{2,0}};
    assert(sol.validPath(3, edges4, 0, 2) == true);

    vector<vector<int>> edges5 = {};
    assert(sol.validPath(1, edges5, 0, 0) == true);

    cout << "All test cases passed." << endl;
    return 0;
}