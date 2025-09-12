#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
  static int searchCeilingOfANumber(const std::vector<int>& arr, int key) {
    if (arr.empty())
      return -1;
    
    int left = 0;
    int right = arr.size() - 1;
    int ceiling = -1;

    while (left <= right) {
      const int mid = left + (right - left) / 2;

      if (arr[mid] == key) {
        return mid;
      } else if (arr[mid] < key) {
        left = mid + 1;
       } else if (arr[mid] > key) {
        ceiling = mid;
        right = mid - 1;
      }
    }

    return ceiling;
  }
};

int main() {
    Solution s;

    std::vector<int> arr1 {4, 6, 10};
    int key1 = 6;
    assert(s.searchCeilingOfANumber(arr1, key1) == 1);

    std::vector<int> arr2 {1, 3, 8, 10, 15};
    int key2 = 12;
    assert(s.searchCeilingOfANumber(arr2, key2) == 4);

    std::vector<int> arr3 {4, 6, 10};
    int key3 = 17;
    assert(s.searchCeilingOfANumber(arr3, key3) == -1);

    std::vector<int> arr4 {4, 6, 10};
    int key4 = -1;
    assert(s.searchCeilingOfANumber(arr4, key4) == 0);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
