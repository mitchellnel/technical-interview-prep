#include <cassert>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

class Solution {
   public:
    int findMaxSumSubArray(const int K, const vector<int>& arr) {
        int maxSum = std::numeric_limits<int>::min();

        int windowStart = 0;
        int windowSum = 0;

        for (int windowEnd = 0; windowEnd < arr.size(); windowEnd++) {
            windowSum += arr[windowEnd];

            if (windowEnd >= K - 1) {
                maxSum = std::max(maxSum, windowSum);

                windowSum -= arr[windowStart];
                windowStart++;
            }
        }

        return maxSum;
    }
};

int main() {
    Solution sol;

    assert(sol.findMaxSumSubArray(3, {2, 1, 5, 1, 3, 2}) == 9);
    assert(sol.findMaxSumSubArray(2, {2, 3, 4, 1, 5}) == 7);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
