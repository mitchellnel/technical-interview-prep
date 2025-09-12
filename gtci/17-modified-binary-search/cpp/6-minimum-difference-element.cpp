#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

class Solution {
public:
  static int searchMinDiffElement(const std::vector<int>& arr, int key) {
    if (arr.empty())
      return -1;
    
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
      const int mid = left + (right - left) / 2;

      if (arr[mid] == key) {
        return arr[mid];
      } else if (arr[mid] < key) {
        left = mid + 1;
      } else if (arr[mid] > key) {
        right = mid - 1;
      }
    }

    // after the loop:
    //  - left points to the largest element > key
    //  - right points to the smallest element < key
    if (left >= arr.size())
      return arr[right];
    if (right < 0)
      return arr[left];
    
    if (std::abs(arr[left] - key) < std::abs(arr[right] - key))
      return arr[left];
    else
      return arr[right];
  }
};

int main() {
    Solution sol;

    assert(sol.searchMinDiffElement({4, 6, 10}, 7) == 6);
    assert(sol.searchMinDiffElement({4, 6, 10}, 4) == 4);
    assert(sol.searchMinDiffElement({1, 3, 8, 10, 15}, 12) == 10);
    assert(sol.searchMinDiffElement({1, 3, 8, 10, 15}, 13) == 15);
    assert(sol.searchMinDiffElement({1, 3, 8, 10, 15}, -1) == 1);

    std::cout << "All test cases passed." << std::endl;
}
