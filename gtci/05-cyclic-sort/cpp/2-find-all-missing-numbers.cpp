#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> findNumbers(vector<int> &&nums) {
        vector<int> missingNumbers;

        size_t i = 0;
        while (i < nums.size()) {
            size_t correctPosition = static_cast<int>(nums[i] - 1);

            // if the number at i is already in it's correct position, then this
            // is a duplicate, so no need to swap
            if (nums[i] != nums[correctPosition]) {
                std::swap(nums[i], nums[correctPosition]);
            } else {
                i++;
            }
        }

        for (i = 0; i < nums.size(); i++) {
            if (i + 1 != nums[i]) missingNumbers.push_back(i + 1);
        }

        return missingNumbers;
    }
};

int main() {
    Solution sol;

    assert(sol.findNumbers({2, 3, 1, 8, 2, 3, 5, 1}) == vector<int>({4, 6, 7}));
    assert(sol.findNumbers({2, 4, 1, 2}) == vector<int>({3}));
    assert(sol.findNumbers({2, 3, 2, 1}) == vector<int>({4}));

    cout << "All test cases passed." << endl;

    return 0;
}
