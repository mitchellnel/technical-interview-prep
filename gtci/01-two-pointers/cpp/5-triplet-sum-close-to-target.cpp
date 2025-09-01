#include <algorithm>
#include <cassert>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

class Solution {
   public:
    int searchTriplet(vector<int>& arr, int targetSum) {
        sort(arr.begin(), arr.end());

        int closestSum = 0;
        int closestDistance = numeric_limits<int>::max();

        for (int i = 0; i < arr.size(); i++) {
            const int firstNum = arr[i];

            vector<int>::const_iterator leftItr = arr.cbegin() + i + 1;
            vector<int>::const_iterator rightItr = arr.cend() - 1;

            while (leftItr < rightItr) {
                const int currentSum = firstNum + *leftItr + *rightItr;
                const int currentDistance = abs(targetSum - currentSum);

                if (currentSum == targetSum) return currentSum;

                if (currentDistance < closestDistance ||
                    (currentDistance <= closestDistance &&
                     currentSum < closestSum)) {
                    closestSum = currentSum;
                    closestDistance = currentDistance;
                }

                if (currentSum < targetSum)
                    leftItr++;
                else if (currentSum > targetSum)
                    rightItr--;
            }
        }
        return closestSum;
    }
};

int main() {
    Solution sol;
    std::vector<int> arr1 = {-2, 0, 1, 2};
    assert(sol.searchTriplet(arr1, 2) == 1);

    std::vector<int> arr2 = {1, 0, 1, 1};
    assert(sol.searchTriplet(arr2, 100) == 3);

    std::vector<int> arr3 = {0, 0, 0};
    assert(sol.searchTriplet(arr3, 1) == 0);

    return 0;
}
