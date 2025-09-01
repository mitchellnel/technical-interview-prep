#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    int findSubarrays(vector<int>&& nums, int target) {
        if (target < 1) return 0;

        int totalCount = 0;

        int windowStart = 0;
        int windowProduct = 1;
        for (int windowEnd = 0; windowEnd < nums.size(); windowEnd++) {
            windowProduct *= nums[windowEnd];

            while (windowStart < nums.size() && windowProduct >= target) {
                windowProduct /= nums[windowStart];

                windowStart++;
            }

            if (windowProduct < target)
                totalCount += windowEnd - windowStart + 1;
        }

        return totalCount;
    }
};

int main() {
    Solution sol;

    assert(sol.findSubarrays(vector<int>({2, 5, 3, 10}), 30) == 6);
    assert(sol.findSubarrays(vector<int>({8, 2, 6, 5}), 50) == 7);
    assert(sol.findSubarrays(vector<int>({10, 5, 2, 6}), 0) == 0);
    assert(sol.findSubarrays(vector<int>({2}), 1) == 0);

    cout << "All test cases passed." << endl;
    return 0;
}
