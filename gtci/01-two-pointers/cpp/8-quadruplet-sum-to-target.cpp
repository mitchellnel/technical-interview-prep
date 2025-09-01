#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    static vector<vector<int>> searchQuadruplets(vector<int> &&arr,
                                                 int target) {
        vector<vector<int>> quadruplets;

        if (arr.size() < 4) return quadruplets;

        std::sort(arr.begin(), arr.end());

        for (auto firstItr = arr.cbegin(); firstItr < arr.cend(); firstItr++) {
            if (firstItr > arr.cbegin() && *firstItr == *(firstItr - 1))
                continue;

            for (auto secondItr = firstItr + 1; secondItr < arr.cend();
                 secondItr++) {
                if (secondItr > firstItr + 1 && *secondItr == *(secondItr - 1))
                    continue;

                auto left = secondItr + 1;
                auto right = arr.cend() - 1;

                while (left < right) {
                    const int currentSum =
                        *firstItr + *secondItr + *left + *right;

                    if (currentSum < target) {
                        left++;
                        while (left < right && *left == *(left - 1)) left++;
                    } else if (currentSum > target) {
                        right--;
                        while (left < right && *right == *(right + 1)) right--;
                    } else {
                        quadruplets.push_back(
                            vector<int>{*firstItr, *secondItr, *left, *right});

                        left++;
                        while (left < right && *left == *(left - 1)) left++;

                        right--;
                        while (left < right && *right == *(right + 1)) right--;
                    }
                }
            }
        }

        return quadruplets;
    }
};

int main() {
    Solution sol;

    assert(sol.searchQuadruplets(vector<int>{4, 1, 2, -1, 1, -3}, 1) ==
           vector<vector<int>>({{-3, -1, 1, 4}, {-3, 1, 1, 2}}));
    assert(sol.searchQuadruplets(vector<int>{2, 0, -1, 1, -2, 2}, 2) ==
           vector<vector<int>>({{-2, 0, 2, 2}, {-1, 0, 1, 2}}));
    assert(sol.searchQuadruplets(vector<int>{0, 0, 0, 0}, 0) ==
           vector<vector<int>>({{0, 0, 0, 0}}));
    cout << "All test cases passed." << endl;

    return 0;
}
