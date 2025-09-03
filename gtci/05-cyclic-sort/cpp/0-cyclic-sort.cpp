#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> sort(vector<int> &&nums) {
        size_t i = 0;

        while (i < nums.size()) {
            int num = nums[i];

            if (i + 1 != static_cast<int>(num)) {
                std::swap(nums[i], nums[num - 1]);
            } else {
                i++;
            }
        }

        return nums;
    }
};

int main() {
    Solution sol;

    assert(sol.sort(vector<int>{3, 1, 5, 4, 2}) ==
           vector<int>({1, 2, 3, 4, 5}));
    assert(sol.sort(vector<int>{2, 6, 4, 3, 1, 5}) ==
           vector<int>({1, 2, 3, 4, 5, 6}));
    assert(sol.sort(vector<int>{1, 5, 6, 4, 3, 2}) ==
           vector<int>({1, 2, 3, 4, 5, 6}));

    cout << "All test cases passed." << endl;

    return 0;
}
