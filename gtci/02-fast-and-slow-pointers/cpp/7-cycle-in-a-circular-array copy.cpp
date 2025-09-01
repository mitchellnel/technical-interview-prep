#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    bool loopExists(const vector<int>& arr) {
        for (int i = 0; i < arr.size(); i++) {
            if (hasCycle(arr, i)) {
                return true;
            }
        }

        return false;
    }

   private:
    static bool hasCycle(const vector<int>& arr, const int& start) {
        const bool is_forward = arr[start] > 0;

        int slow = start;
        int fast = start;
        for (;;) {
            slow = Solution::getNextIndex(arr, is_forward, slow);

            fast = Solution::getNextIndex(arr, is_forward, fast);
            if (fast != -1)
                fast = Solution::getNextIndex(arr, is_forward, fast);

            if (slow == -1 || fast == -1 || slow == fast) break;
        }

        return slow != -1 && slow == fast;
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
