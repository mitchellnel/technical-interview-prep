#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<vector<int>> findSubarrays(const vector<int>& arr, int target) {
        if (target < 1) return vector<vector<int>>();

        vector<vector<int>> result;

        int windowStart = 0;
        int windowProduct = 1;
        for (int windowEnd = 0; windowEnd < arr.size(); windowEnd++) {
            windowProduct *= arr[windowEnd];

            while (windowStart < arr.size() && windowProduct >= target) {
                windowProduct /= arr[windowStart];

                windowStart++;
            }

            int subarraySlider = windowEnd;
            while (subarraySlider >= windowStart) {
                vector<int> subarray;
                for (int i = subarraySlider; i <= windowEnd; i++)
                    subarray.push_back(arr[i]);

                result.push_back(subarray);

                subarraySlider--;
            }
        }

        return result;
    }
};

int main() {
    Solution sol;

    vector<vector<int>> result;

    result = sol.findSubarrays(vector<int>({2, 5, 3, 10}), 30);
    assert(result ==
           vector<vector<int>>({{2}, {5}, {2, 5}, {3}, {5, 3}, {10}}));

    result = sol.findSubarrays(vector<int>({8, 2, 6, 5}), 50);
    assert(result == vector<vector<int>>({
                         {8},
                         {2},
                         {8, 2},
                         {6},
                         {2, 6},
                         {5},
                         {6, 5},
                     }));

    cout << "All test cases passed." << endl;
    return 0;
}
