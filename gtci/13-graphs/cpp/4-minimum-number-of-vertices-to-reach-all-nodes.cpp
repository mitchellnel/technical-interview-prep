#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> findSmallestSetOfVertices(int n, std::vector<std::vector<int>>& edges) {
        std::vector<int> indegrees (n, 0);
        
        for (const auto& edge : edges) {
            indegrees[edge[1]] += 1;
        }

        std::vector<int> result;
        for (int i = 0; i < n; ++i) {
            if (indegrees[i] == 0) result.push_back(i);
        }

        return result;
    }
};

int main() {
    Solution s;

    std::vector<std::vector<int>> edges1 = {{0,1}, {0,2}, {2,5}, {3,4}, {4,2}};
    assert(s.findSmallestSetOfVertices(6, edges1) == std::vector<int>({0,3}));

    std::vector<std::vector<int>> edges2 = {{0,1}, {2,1}, {3,1}, {1,4}, {2,4}};
    assert(s.findSmallestSetOfVertices(5, edges2) == std::vector<int>({0,2,3}));

    std::vector<std::vector<int>> edges3 = {};
    assert(s.findSmallestSetOfVertices(3, edges3) == std::vector<int>({0,1,2}));

    std::vector<std::vector<int>> edges4 = {{0,1}, {1,2}, {2,0}};
    assert(s.findSmallestSetOfVertices(3, edges4) == std::vector<int>({}));

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
