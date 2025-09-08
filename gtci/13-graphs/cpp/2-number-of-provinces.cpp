#include <cassert>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    int findProvinces(vector<vector<int>>& isConnected) {
        std::vector<bool> visited (isConnected.size(), false);
        int numProvinces = 0;

        for (int i = 0; i < isConnected.size(); i++) {
            if (!visited[i]) {
                numProvinces++;

                dfs(i, visited, isConnected);
            }
        }

        return numProvinces;
    }

private:
    void dfs(const int& node, std::vector<bool>& visited, const std::vector<std::vector<int>>& isConnected) {
        std::stack<int> stack;
        stack.push(node);

        while (!stack.empty()) {
            const int curr = stack.top();
            stack.pop();

            visited[curr] = true;

            for (int v = 0; v < isConnected[curr].size(); v++) {
                if (isConnected[curr][v] == 1 && !visited[v])
                    stack.push(v);
            }
        }
    }
};

int main() {
    Solution sol;

    vector<vector<int>> isConnected1 = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
    assert(sol.findProvinces(isConnected1) == 2);

    vector<vector<int>> isConnected2 = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    assert(sol.findProvinces(isConnected2) == 3);

    vector<vector<int>> isConnected3 = {{1, 0, 0, 1}, {0, 1, 1, 0}, {0, 1, 1, 0}, {1, 0, 0, 1}};
    assert(sol.findProvinces(isConnected3) == 2);

    cout << "All test cases passed." << endl;
    return 0;
}
