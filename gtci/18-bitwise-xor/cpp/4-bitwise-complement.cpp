#include <cassert>
#include <iostream>

class Solution {
public:
  int bitwiseComplement(int num) {
    int mask = 1;
    while (mask <= num)
      mask <<= 1;
    mask -= 1;

    return num ^ mask;
  }
};

int main() {
    Solution s;

    assert(s.bitwiseComplement(5) == 2);
    assert(s.bitwiseComplement(7) == 0);
    assert(s.bitwiseComplement(10) == 5);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
