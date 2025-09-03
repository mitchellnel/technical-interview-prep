#include <cassert>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> findNumbers(vector<int>&& nums) {
        size_t i = 0;
        while (i < nums.size()) {
            size_t correctPosition = nums[i] - 1;

            if (nums[i] != nums[correctPosition]) {
                std::swap(nums[i], nums[correctPosition]);
            } else {
                i++;
            }
        }

        for (i = 0; i < nums.size(); i++) {
            if (i + 1 != nums[i])
                return vector<int>{nums[i], static_cast<int>(i + 1)};
        }
        return vector<int>{-1, -1};
    }
};

int main() {
    Solution sol;

    assert(sol.findNumbers({3, 1, 2, 5, 2}) == vector<int>({2, 4}));
    assert(sol.findNumbers({3, 1, 2, 3, 6, 4}) == vector<int>({3, 5}));

    cout << "All test cases passed." << endl;

    return 0;
}
