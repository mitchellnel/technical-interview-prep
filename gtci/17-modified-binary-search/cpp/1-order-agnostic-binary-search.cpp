#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
  int search(const std::vector<int>& arr, int key) {
    if (arr.empty())
      return -1;
    
    const bool isAscending = arr[0] <= arr[arr.size() - 1];

    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
      const int mid = left + (right - left) / 2;    // avoid potential overflow

      if (arr[mid] == key)
        return mid;
      else if ((isAscending && arr[mid] < key) || (!isAscending && arr[mid] > key))
        left = mid + 1;
      else if ((isAscending && arr[mid] > key) || (!isAscending && arr[mid] < key))
        right = mid - 1;
    }
    
    return -1;  // element not found
  }
};

int main() {
    Solution s;
    
    // ascending order
    std::vector<int> arr1 {4, 6, 10};
    int key1 = 10;
    assert(s.search(arr1, key1) == 2);

    // descending order
    std::vector<int> arr2 {10, 6, 4};
    int key2 = 10;
    assert(s.search(arr2, key2) == 0);
    
    // element not found
    std::vector<int> arr3 {10, 6, 4};
    int key3 = 5;
    assert(s.search(arr3, key3) == -1);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
