#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
  int countRotations(const std::vector<int>& arr) {
    // rotation count == index of smallest element
    // smallest element is the only element whose previous is greater than itself
    int left = 0;
    int right = arr.size() - 1;

    while (left < right) {
      const int mid = left + (right - left) / 2;

      if (arr[left] == arr[mid] && arr[mid] == arr[right]) {
        // if there are duplicates we can't be sure which side to go to
        // so skip an index for both UNLESS one of them is the min
        if (arr[left] > arr[left + 1])
          return left + 1;
        left++;

        if (arr[right] < arr[right - 1])
          return right;
        right--;
      }

      if (mid > left && arr[mid - 1] > arr[mid])
        return mid;

      if (mid < right && arr[mid] > arr[mid + 1])
        return mid + 1;

      if (arr[left] < arr[mid]) {
        // min is either at mid or to the right of mid
        left = mid + 1;
      } else {
        // min is either at mid or to the left of mid
        right = mid - 1;
      }
    }

    return 0;
  }
};

int main() {
    Solution s;
    
    assert(s.countRotations({15, 18, 2, 3, 6, 12}) == 2);
    assert(s.countRotations({7, 9, 11, 12, 5}) == 4);
    assert(s.countRotations({7, 9, 11, 12, 15}) == 0);
    assert(s.countRotations({2, 3, 6, 12, 15, 18}) == 0);
    assert(s.countRotations({3, 6, 12, 15, 18, 2}) == 5);
    
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
