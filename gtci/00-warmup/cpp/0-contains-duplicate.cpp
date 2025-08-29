#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
   public:
    bool containsDuplicate(vector<int> &nums) {
        unordered_set<int> appears{};

        for (int num : nums) {
            /* Solution 1: average O(1), two hash lookups */
            // if (!appears.contains(num)) {
            //     appears.insert(num);
            //     continue;
            // }

            // return true;

            /* Solution 2: average O(n), one hash lookup; in theory slightly
             * faster */
            // size_t initialSize = appears.size();
            // appears.insert(num);

            // if (appears.size() == initialSize) {
            //     return true;
            // }

            /* Solution 3: average O(n), same as above but in theory even faster
             * due to no branch from the if statement */
            auto [_, inserted] = appears.insert(num);

            if (!inserted) return true;
        }

        return false;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 1};
    cout << (sol.containsDuplicate(nums) ? "true" : "false")
         << endl;  // Output: true
    nums = {1, 2, 3, 4};
    cout << (sol.containsDuplicate(nums) ? "true" : "false")
         << endl;  // Output: false
    nums = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
    cout << (sol.containsDuplicate(nums) ? "true" : "false")
         << endl;  // Output: true
    return 0;
}
