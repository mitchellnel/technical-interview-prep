#include <cassert>
#include <climits>
#include <iostream>
#include <limits>
#include <vector>

class ArrayReader {
public:
  std::vector<int> arr;

  ArrayReader(const std::vector<int> &arr) { this->arr = arr; }

  virtual int get(int index) {
    if (index >= arr.size()) {
      return std::numeric_limits<int>::max();
    }
    return arr[index];
  }
};

class Solution {
public:
  static int searchInfiniteSortedArray(ArrayReader reader, int key) {
    int left = 0;
    int right = 1;

    // find a finite sized window to do the search
    while (reader.get(right) < key) {
      left = right;
      right *= 2;
    }

    // peform the search
    while (left <= right) {
      const int mid = left + (right - left) / 2;

      if (reader.get(mid) == key)
        return mid;
      else if (reader.get(mid) < key)
        left = mid + 1;
      else if (reader.get(mid) > key)
        right = mid - 1;
    }

    return -1;
  }
};

int main() {
    Solution s;

    ArrayReader reader1({4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30});
    int key1 = 16;
    assert(s.searchInfiniteSortedArray(reader1, key1) == 6);

    ArrayReader reader2({1, 3, 8, 10, 15});
    int key2 = 15;
    assert(s.searchInfiniteSortedArray(reader2, key2) == 4);

    ArrayReader reader3({1, 3, 8, 10, 15});
    int key3 = 200;
    assert(s.searchInfiniteSortedArray(reader3, key3) == -1);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
