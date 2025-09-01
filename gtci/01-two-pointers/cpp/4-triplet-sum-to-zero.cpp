#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    static vector<vector<int>> searchTriplets(vector<int>& arr) {
        vector<vector<int>> triplets;

        sort(arr.begin(), arr.end());

        for (int i = 0; i < arr.size(); i++) {
            const int firstNum = arr[i];

            if (i > 0 && arr[i - 1] == firstNum) continue;

            vector<int>::const_iterator leftItr = arr.cbegin() + i + 1;
            vector<int>::const_iterator rightItr = arr.cend() - 1;

            while (leftItr < rightItr) {
                const int total_sum = firstNum + *leftItr + *rightItr;

                if (total_sum < 0) {
                    leftItr++;
                } else if (total_sum > 0) {
                    rightItr--;
                } else {
                    const vector<int> triplet{firstNum, *leftItr, *rightItr};
                    triplets.push_back(triplet);

                    leftItr++;
                    while (leftItr < rightItr && *(leftItr - 1) == *leftItr)
                        leftItr++;

                    rightItr--;
                    while (leftItr < rightItr && *(rightItr + 1) == *rightItr)
                        rightItr--;
                }
            }
        }

        return triplets;
    }
};

bool tripletVectorsEqual(const std::vector<std::vector<int>>& a,
                         const std::vector<std::vector<int>>& b) {
    if (a.size() != b.size()) return false;
    auto sortedA = a, sortedB = b;
    for (auto& v : sortedA) std::sort(v.begin(), v.end());
    for (auto& v : sortedB) std::sort(v.begin(), v.end());
    std::sort(sortedA.begin(), sortedA.end());
    std::sort(sortedB.begin(), sortedB.end());
    return sortedA == sortedB;
}

int main() {
    Solution sol;
    std::vector<int> arr1 = {-2, -1, 0, 1, 2};
    auto result1 = sol.searchTriplets(arr1);
    std::vector<std::vector<int>> expected1 = {{-2, 0, 2}, {-1, 0, 1}};
    assert(tripletVectorsEqual(result1, expected1));

    std::vector<int> arr2 = {-1, 0, 1, 2, -1, -4};
    auto result2 = sol.searchTriplets(arr2);
    std::vector<std::vector<int>> expected2 = {{-1, -1, 2}, {-1, 0, 1}};
    assert(tripletVectorsEqual(result2, expected2));

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
