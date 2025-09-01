#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    int findLength(const vector<int> &arr, int k) {
        int maxLength = 0;

        int windowStart = 0;
        int zeroCount = 0;
        for (int windowEnd = 0; windowEnd < arr.size(); windowEnd++) {
            int windowSize = windowEnd - windowStart + 1;

            if (arr[windowEnd] == 0) zeroCount++;

            if (zeroCount <= k) maxLength = std::max(maxLength, windowSize);

            if (zeroCount > k) {
                if (arr[windowStart] == 0) zeroCount--;

                windowStart++;
                windowSize = windowEnd - windowStart + 1;
            }
        }

        return maxLength;
    }
};

int main() {
    Solution sol;

    assert(sol.findLength({0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1}, 2) == 6);
    assert(sol.findLength({0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1}, 3) == 9);
    assert(sol.findLength({1, 0, 0, 1, 1, 0, 1, 1}, 2) == 6);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
