#include <algorithm>
#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> findNumbers(vector<int>&& nums) {
        vector<int> duplicateNumbers;

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
            if (i + 1 != nums[i]) duplicateNumbers.push_back(nums[i]);
        }

        return duplicateNumbers;
    }
};

int main() {
    Solution sol;

    assert(sol.findNumbers({3, 4, 4, 5, 5}) == vector<int>({5, 4}));
    assert(sol.findNumbers({5, 4, 7, 2, 3, 5, 3}) == vector<int>({3, 5}));

    cout << "All test cases passed." << endl;

    return 0;
}
