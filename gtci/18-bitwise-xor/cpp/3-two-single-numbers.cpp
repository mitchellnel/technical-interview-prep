#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
  std::vector<int> findSingleNumbers(const std::vector<int>& nums) {
    int xorAll = 0;
    for (int num : nums)
      xorAll ^= num;

    // find the rightmost bit of xorAll
    // this is the rightmost bit where the two numbers differ
    const int rightmostBit = xorAll & -xorAll;

    // sort nums by the rightmost bit
    int xor1 = 0;
    int xor2 = 0;
    for (int num : nums) {
      if ((num & rightmostBit) != 0)
        xor1 ^= num;
      else
        xor2 ^= num;
    }

    return std::vector<int> {xor1, xor2};
  }
};

int main() {
    Solution s;
    
    auto result1 = s.findSingleNumbers({1, 4, 2, 1, 3, 2});
    assert((result1 == std::vector<int>{3, 4} || result1 == std::vector<int>{4, 3}));
    
    auto result2 = s.findSingleNumbers({1, 2, 3, 2});
    assert((result2 == std::vector<int>{1, 3} || result2 == std::vector<int>{3, 1}));
    
    auto result3 = s.findSingleNumbers({1, 2});
    assert((result3 == std::vector<int>{1, 2} || result3 == std::vector<int>{2, 1}));
    
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
