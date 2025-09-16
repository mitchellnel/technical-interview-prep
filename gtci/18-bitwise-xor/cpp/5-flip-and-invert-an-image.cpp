#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

class Solution {
  public:
    std::vector<std::vector<int>> flipAndInvertImage(std::vector<std::vector<int>> arr) {
      for (std::vector<int>& row : arr) {
        size_t left = 0;
        size_t right = row.size() - 1;

        while (left <= right) {
          // flip
          std::swap(row[left], row[right]);

          // invert
          row[left] ^= 1;
        
          if (left != right)
            row[right] ^= 1;

          left++;
          right--;
        }
      }

      return arr;
    }
};

int main() {
    Solution s;

    auto result1 = s.flipAndInvertImage({{1,1,0},{1,0,1},{0,0,0}});
    std::vector<std::vector<int>> expected1 = {{1,0,0},{0,1,0},{1,1,1}};
    assert(result1 == expected1);

    auto result2 = s.flipAndInvertImage({{1,1,0,0},{1,0,0,1},{0,1,1,1},{1,0,1,0}});
    std::vector<std::vector<int>> expected2 = {{1,1,0,0},{0,1,1,0},{0,0,0,1},{1,0,1,0}};
    assert(result2 == expected2);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
