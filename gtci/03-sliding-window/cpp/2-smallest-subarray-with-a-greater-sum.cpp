#include <algorithm>
#include <cassert>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

class Solution {
   public:
    int findMinSubArray(int S, const vector<int>& arr) {
        int minSubarraySize = std::numeric_limits<int>::max();

        int windowStart = 0;
        int windowSum = 0;

        for (int windowEnd = 0; windowEnd < arr.size(); windowEnd++) {
            windowSum += arr[windowEnd];

            while (windowSum >= S) {
                minSubarraySize =
                    std::min(minSubarraySize, windowEnd - windowStart + 1);

                windowSum -= arr[windowStart];
                windowStart++;
            }
        }

        return minSubarraySize != std::numeric_limits<int>::max()
                   ? minSubarraySize
                   : 0;
    }
};

int main() {
    Solution sol;

    assert(sol.findMinSubArray(7, {2, 1, 5, 2, 3, 2}) == 2);
    assert(sol.findMinSubArray(7, {2, 1, 5, 2, 8}) == 1);
    assert(sol.findMinSubArray(8, {3, 4, 1, 1, 6}) == 3);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
