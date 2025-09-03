#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution {
   public:
    static int findMissingNumber(vector<int> &&nums) {
        size_t i = 0;
        while (i < nums.size()) {
            int num = nums[i];

            if (num < nums.size() && i != num) {
                std::swap(nums[i], nums[num]);
            } else {
                i++;
            }
        }

        for (i = 0; i < nums.size(); i++) {
            if (i != nums[i]) return i;
        }

        return nums.size();
    }
};

int main() {
    Solution sol;

    assert(sol.findMissingNumber(vector<int>{3, 0, 1}) == 2);
    assert(sol.findMissingNumber(vector<int>{0, 1}) == 2);
    assert(sol.findMissingNumber(vector<int>{9, 6, 4, 2, 3, 5, 7, 0, 1}) == 8);

    cout << "All test cases passed." << endl;

    return 0;
}
