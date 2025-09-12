#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
  int search(const std::vector<int>& arr, int key) {
    if (arr.empty())
      return -1;
    
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
      const int mid = left + (right - left) / 2;

      if (arr[mid] == key)
        return mid;

      // duplicates, we don't know which side is sorted, so move left and right up by one
      if (arr[left] == arr[mid] && arr[right] == arr[mid]) {
        left++;
        right--;
        continue;
      }

      if (arr[left] <= arr[mid]) {
        // first half is sorted
        if (key >= arr[left] && key < arr[mid])   // target is in first half
          right = mid - 1;
        else
          left = mid + 1;                          // target is in second half
      } else {
        // second half is sorted
        if (key > arr[mid] && key <= arr[right])
          left = mid + 1;                          // target is in second half
        else
          right = mid - 1;                         // target is in first half
      }
    }

    return -1;
  }
};

int main() {
    Solution s;
    
    std::vector<int> arr1 {10, 15, 1, 3, 8};
    assert(s.search(arr1, 15) == 1);
    assert(s.search(arr1, 10) == 0);
    assert(s.search(arr1, 8) == 4);
    assert(s.search(arr1, 12) == -1);
    
    std::vector<int> arr2 {4, 5, 7, 9, 10, -1, 2};
    assert(s.search(arr2, 10) == 4);
    assert(s.search(arr2, -1) == 5);
    assert(s.search(arr2, 4) == 0);
    assert(s.search(arr2, 6) == -1);
    
    std::vector<int> arr3 {1};
    assert(s.search(arr3, 1) == 0);
    assert(s.search(arr3, 0) == -1);

    std::vector<int> arr4 {3, 7, 3, 3, 3};
    assert(s.search(arr4, 7) == 1);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
