#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
  std::vector<int> findRange(const std::vector<int>& arr, int key) {
    return {findFirstOccurrence(arr, key), findLastOccurrence(arr, key)};
  }
private:
  int findFirstOccurrence(const std::vector<int>& arr, const int& key) {
    int left = 0;
    int right = arr.size() - 1;

    int first = -1;

    while (left <= right) {
      const int mid = left + (right - left) / 2;

      if (arr[mid] == key) {
        first = mid;
        right = mid - 1;
      } else if (arr[mid] < key) {
        left = mid + 1;
      } else if (arr[mid] > key) {
        right = mid - 1;
      }
    }

    return first;
  }

  int findLastOccurrence(const std::vector<int>& arr, const int& key) {
    int left = 0;
    int right = arr.size() - 1;

    int last = -1;

    while (left <= right) {
      const int mid = left + (right - left) / 2;

      if (arr[mid] == key) {
        last = mid;
        left = mid + 1;
      } else if (arr[mid] < key) {
        left = mid + 1;
      } else if (arr[mid] > key) {
        right = mid - 1;
      }
    }

    return last;
  }
};

int main() {
    Solution s;

    std::vector<int> arr1 {4, 6, 6, 6, 9};
    int key1 = 6;
    std::vector<int> result1 = s.findRange(arr1, key1);
    assert((result1 == std::vector<int>{1, 3}));

    std::vector<int> arr2 {1, 3, 8, 10, 15};
    int key2 = 10;
    std::vector<int> result2 = s.findRange(arr2, key2);
    assert((result2 == std::vector<int>{3, 3}));

    std::vector<int> arr3 {1, 3, 8, 10, 15};
    int key3 = 12;
    std::vector<int> result3 = s.findRange(arr3, key3);
    assert((result3 == std::vector<int>{-1, -1}));

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
