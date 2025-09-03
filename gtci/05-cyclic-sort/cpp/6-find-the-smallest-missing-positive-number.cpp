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
            int correctPosition = nums[i] - 1;

            if (correctPosition < nums.size() && nums[i] >= 1 &&
                nums[i] != nums[correctPosition]) {
                std::swap(nums[i], nums[correctPosition]);
            } else {
                i++;
            }
        }

        for (i = 0; i < nums.size(); i++) {
            if (i + 1 != nums[i]) return i + 1;
        }

        return nums.size() + 1;
    }
};

int main() {
    Solution sol;

    assert(sol.findNumber({-3, 1, 5, 4, 2}) == 3);
    assert(sol.findNumber({3, -2, 0, 1, 2}) == 4);
    assert(sol.findNumber({3, 2, 5, 1}) == 4);
    assert(sol.findNumber({33, 37, 5}) == 1);

    cout << "All test cases passed." << endl;

    return 0;
}
