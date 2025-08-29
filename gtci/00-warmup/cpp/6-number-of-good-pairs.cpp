#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
   public:
    int numGoodPairs(std::vector<int>& nums) {
        int pairCount = 0;
        std::unordered_map<int, int> freq_map{};

        for (int num : nums) {
            pairCount += freq_map[num];
            freq_map[num] += 1;
        }

        return pairCount;
    }
};

int main() {
    Solution sol;
    std::vector<int> nums1 = {1, 2, 3, 1, 1, 3};
    std::cout << sol.numGoodPairs(nums1) << std::endl;  // Output: 4

    std::vector<int> nums2 = {1, 1, 1, 1};
    std::cout << sol.numGoodPairs(nums2) << std::endl;  // Output: 6

    std::vector<int> nums3 = {1, 2, 3};
    std::cout << sol.numGoodPairs(nums3) << std::endl;  // Output: 0

    return 0;
}
