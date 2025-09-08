#include <cassert>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <vector>

using namespace std;

class Graph {
public:
    std::unordered_map<int, std::vector<int>> adjacency_list;

    Graph(const std::unordered_map<int, std::vector<int>>& adjacency_list) {
        this->adjacency_list = adjacency_list;
    }

    std::vector<int> dfs_traversal(int start_node) {
        std::unordered_set<int> visited;
        std::vector<int> traversal;

        dfsTraversalHelper(start_node, visited, traversal);

        return traversal;
    }

    void dfsTraversalHelper(int node, std::unordered_set<int>& visited, std::vector<int>& traversal) {
        traversal.push_back(node);
        visited.insert(node);

        for (int v : adjacency_list[node]) {
            if (!visited.contains(v))
                dfsTraversalHelper(v, visited, traversal);
        }
    }
};

int main() {
    Graph g1({{0, {1,2}}, {1, {0,3}}, {2, {0}}, {3, {1}}});
    auto trav = g1.dfs_traversal(0);
    assert(g1.dfs_traversal(0) == std::vector<int>({0, 1, 3, 2}));

    Graph g2({{0, {1}}, {1, {0}}, {2, {3}}, {3, {2}}});
    assert(g2.dfs_traversal(0) == std::vector<int>({0,1}));
    assert(g2.dfs_traversal(2) == std::vector<int>({2,3}));

    Graph g3(std::unordered_map<int, std::vector<int>>{{0, {}}});
    assert(g3.dfs_traversal(0) == std::vector<int>({0}));

    Graph g4({{0, {1}}, {1, {2}}, {2, {0}}});
    std::vector<int> result4 = g4.dfs_traversal(0);
    assert(result4.size() == 3 && result4[0] == 0 && std::unordered_set<int>(result4.begin(), result4.end()) == std::unordered_set<int>({0,1,2}));

    // tree-shaped graph
    Graph g5({{0, {1,2}}, {1, {3,4}}, {2, {5}}, {3, {}}, {4, {}}, {5, {}}});
    assert(g5.dfs_traversal(0) == std::vector<int>({0, 1, 3, 4, 2, 5}));

    Graph g6({{0, {1,2,3,4}}, {1, {}}, {2, {}}, {3, {}}, {4, {}}});
    assert(g6.dfs_traversal(0) == std::vector<int>({0, 1, 2, 3, 4}));

    cout << "All test cases passed." << endl;

    return 0;
}
