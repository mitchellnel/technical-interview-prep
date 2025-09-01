#include <cassert>
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
   public:
    bool loopExists(const vector<int>& arr) {
        vector<bool> visited(arr.size(), false);
        for (int i = 0; i < arr.size(); i++) {
            if (!visited[i] && hasCycle(arr, i, visited)) {
                return true;
            }
        }

        return false;
    }

   private:
    static bool hasCycle(const vector<int>& arr, const int& start,
                         vector<bool>& visited) {
        unordered_set<int> path{start};

        const bool is_forward = arr[start] > 0;

        int slow = start;
        int fast = start;
        for (;;) {
            slow = Solution::getNextIndex(arr, is_forward, slow);

            fast = Solution::getNextIndex(arr, is_forward, fast);
            if (fast != -1)
                fast = Solution::getNextIndex(arr, is_forward, fast);

            if (slow == -1 || fast == -1) break;

            if (slow == fast) return true;
        }

        // mark all nodes in path as visited
        for (int node : path) visited[node] = true;

        return false;
    }

    static int getNextIndex(const vector<int>& arr, const bool& is_forward,
                            const int curr) {
        const bool is_next_direction_forward = arr[curr] > 0;
        if (is_forward != is_next_direction_forward) return -1;

        const int next = (curr + arr[curr]) % arr.size();

        // is it a 1 element cycle
        if (curr == next) return -1;

        return next;
    }
};

int main() {
    Solution sol;

    assert(sol.loopExists({1, 2, -1, 2, 2}));
    assert(sol.loopExists({2, 2, -1, 2}));
    assert(!sol.loopExists({2, 1, -1, -2}));

    cout << "All test cases passed." << endl;

    return 0;
}
