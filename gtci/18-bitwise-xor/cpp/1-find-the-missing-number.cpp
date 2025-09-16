#include <cassert>
#include <iostream>
#include <vector>

class Solution {
    public:
    int findMissingNumber(const std::vector<int>& nums) {
        const size_t& n = nums.size() + 1;

        int x1 = nums[0];
        for (size_t i = 1; i < nums.size(); i++)
            x1 ^= nums[i];
        
        int x2 = 1;
        for (size_t i = 2; i < n + 1; i++)
            x2 ^= i;
        
        return x1 ^ x2;
    }
};

int main() {
    Solution s;

    assert(s.findMissingNumber({1, 5, 2, 6, 4}) == 3);
    assert(s.findMissingNumber({1, 3}) == 2);
    assert(s.findMissingNumber({10, 6, 4, 2, 3, 5, 7, 8, 1}) == 9);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
