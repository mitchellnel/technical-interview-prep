#include <cassert>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

class Solution {
   public:
    static int sort(const vector<int>& arr) {
        auto left = arr.cbegin() + 1;
        auto right = arr.cend() - 2;

        while (left < arr.cend()) {
            if (*left < *(left - 1)) {
                left--;
                break;
            }

            left++;
        }

        if (left == arr.cend()) return 0;  // array is already sorted

        while (right >= arr.cbegin()) {
            if (*right > *(right + 1)) {
                right++;
                break;
            }

            right--;
        }

        int subarray_min = std::numeric_limits<int>::max();
        int subarray_max = std::numeric_limits<int>::min();
        for (auto itr = left; itr <= right; itr++) {
            subarray_min = std::min(subarray_min, *itr);
            subarray_max = std::max(subarray_max, *itr);
        }

        while (left > arr.cbegin() && *(left - 1) > subarray_min) left--;

        while (right < arr.cend() - 1 && *(right + 1) < subarray_max) right++;

        return right - left + 1;
    }
};

int main() {
    Solution sol;
    assert(sol.sort({1, 2, 5, 3, 7, 10, 9, 12}) == 5);
    assert(sol.sort({1, 3, 2, 0, -1, 7, 10}) == 5);
    assert(sol.sort({1, 2, 3}) == 0);
    assert(sol.sort({3, 2, 1}) == 3);
    assert(sol.sort({3, 3, 2, 2}) == 4);
    cout << "All test cases passed." << endl;

    return 0;
}
