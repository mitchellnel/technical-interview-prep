#include <cassert>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <vector>

using namespace std;


class Graph {
public:
    std::unordered_map<int, std::vector<int>> adjacency_list;

    Graph(const std::unordered_map<int, std::vector<int>>& adjacency_list) {
        this->adjacency_list = adjacency_list;
    }

    std::vector<int> bfs_traversal(int start_node) {
        std::unordered_set<int> visited;
        std::queue<int> queue;
        queue.push(start_node);

        std::vector<int> traversal;

        while (!queue.empty()) {
            const int curr = queue.front();
            queue.pop();

            if (!visited.contains(curr)) {
                visited.insert(curr);
                traversal.push_back(curr);
            }

            for (int node : adjacency_list[curr]) {
                if (!visited.contains(node))
                    queue.push(node);
            }
        }

        return traversal;
    }
};

int main() {
    Graph g1({{0, {1,2}}, {1, {0,3}}, {2, {0}}, {3, {1}}});
    assert(g1.bfs_traversal(0) == std::vector<int>({0,1,2,3}));
    
    Graph g2({{0, {1}}, {1, {0}}, {2, {3}}, {3, {2}}});
    assert(g2.bfs_traversal(0) == std::vector<int>({0,1}));
    assert(g2.bfs_traversal(2) == std::vector<int>({2,3}));
    
    Graph g3(std::unordered_map<int, std::vector<int>>{{0, {}}});
    assert(g3.bfs_traversal(0) == std::vector<int>({0}));
    
    Graph g4({{0, {1}}, {1, {2}}, {2, {0}}});
    std::vector<int> result4 = g4.bfs_traversal(0);
    assert(result4.size() == 3 && result4[0] == 0 && std::unordered_set<int>(result4.begin(), result4.end()) == std::unordered_set<int>({0,1,2}));

    // tree-shaped graph
    Graph g5({{0, {1,2}}, {1, {3,4}}, {2, {5}}, {3, {}}, {4, {}}, {5, {}}});
    assert(g5.bfs_traversal(0) == std::vector<int>({0,1,2,3,4,5}));
    
    Graph g6({{0, {1,2,3,4}}, {1, {}}, {2, {}}, {3, {}}, {4, {}}});
    assert(g6.bfs_traversal(0) == std::vector<int>({0,1,2,3,4}));

    cout << "All test cases passed." << endl;

    return 0;
}
