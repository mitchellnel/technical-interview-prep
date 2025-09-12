#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
  int findMax(const std::vector<int>& arr) {
    if (arr.empty())
      return -1;
    
    int left = 0;
    int right = arr.size() - 1;

    while (left < right) {
      const int mid = left + (right - left) / 2;

      if (mid < arr.size() - 1 && arr[mid] < arr[mid + 1])
        left = mid + 1;
      else
        right = mid;
    }

    return arr[left];
  }
};

int main() {
    Solution sol;

    assert(sol.findMax({1, 3, 8, 12, 4, 2}) == 12);
    assert(sol.findMax({3, 8, 3, 1}) == 8);
    assert(sol.findMax({1, 3, 8, 12}) == 12);
    assert(sol.findMax({10, 9, 8}) == 10);
    assert(sol.findMax({10}) == 10);
    assert(sol.findMax({}) == -1);

    std::cout << "All test cases passed." << std::endl;

}