#include <cassert>
#include <iostream>
#include <vector>

class Solution {
  public:
    int findSingleNumber(const std::vector<int>& arr) {
      int num = arr[0];
      
      for (size_t i = 1; i < arr.size(); i++)
        num ^= arr[i];

      return num;
    }
};

int main() {
    Solution s;

    assert(s.findSingleNumber({2, 3, 5, 4, 5, 3, 4}) == 2);
    assert(s.findSingleNumber({1, 1, 2}) == 2);
    assert(s.findSingleNumber({1}) == 1);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
