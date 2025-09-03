#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution {
   public:
    int findNumber(vector<int>&& nums) {
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
            if (i + 1 != nums[i]) return nums[i];
        }

        return -1;
    }

    int findNumberAlternate(vector<int>&& nums) {
        size_t i = 0;
        while (i < nums.size()) {
            if (nums[i] != i + 1) {
                size_t correctPosition = nums[i] - 1;

                if (nums[i] == nums[correctPosition]) {
                    return nums[i];
                } else {
                    std::swap(nums[i], nums[correctPosition]);
                }
            } else {
                i++;
            }
        }
    }
};

int main() {
    Solution sol;

    assert(sol.findNumber({1, 4, 4, 3, 2}) == 4);
    assert(sol.findNumber({2, 1, 3, 3, 5, 4}) == 3);
    assert(sol.findNumber({2, 4, 1, 4, 4}) == 4);

    cout << "All test cases passed." << endl;

    return 0;
}
