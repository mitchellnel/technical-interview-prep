#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
  int search(const std::vector<int>& arr, int key) {
    if (arr.empty())
      return -1;

    const int bitonicMaxIndex = findBitonicMaxIndex(arr);

    const int firstHalfKeyIndex = increasingBinarySearch(arr, key, 0, bitonicMaxIndex);
    if (firstHalfKeyIndex != -1)
      return firstHalfKeyIndex;
    
    return decreasingBinarySearch(arr, key, bitonicMaxIndex + 1, arr.size() - 1);
  }
private:
  int findBitonicMaxIndex(const std::vector<int>& arr) {
    int left = 0;
    int right = arr.size() - 1;

    while (left < right) {
      const int mid = left + (right - left) / 2;

      if (arr[mid] < arr[mid + 1])
        left = mid + 1;
      else
        right = mid;
    }

    return left;
  }

  int increasingBinarySearch(const std::vector<int>& arr, const int& key, int left, int right) {
    while (left <= right) {
      const int mid = left + (right - left) / 2;

      if (arr[mid] == key)
        return mid;
      else if (arr[mid] < key)
        left = mid + 1;
      else
        right = mid - 1;
    }

    return -1;
  }

  int decreasingBinarySearch(const std::vector<int>& arr, const int& key, int left, int right) {
    while (left <= right) {
      const int mid = left + (right - left) / 2;

      if (arr[mid] == key)
        return mid;
      else if (arr[mid] > key)
        left = mid + 1;
      else
        right = mid - 1;
    }

    return -1;
  }
};

int main() {
    Solution sol;

    assert(sol.search({1, 3, 8, 4, 3}, 4) == 3);
    assert(sol.search({3, 8, 3, 1}, 8) == 1);
    assert(sol.search({1, 3, 8, 12, 4, 2}, 12) == 3);
    assert(sol.search({1, 3, 8, 12, 4, 2}, 4) == 4);
    assert(sol.search({1, 3, 8, 12, 4, 2}, 6) == -1);
    assert(sol.search({10, 9, 8}, 10) == 0);
    assert(sol.search({10, 9, 8}, 8) == 2);
    assert(sol.search({10, 9, 8}, 9) == 1);
    assert(sol.search({10}, 10) == 0);
    assert(sol.search({}, 10) == -1);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
