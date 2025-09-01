#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    int searchTriplets(vector<int> &&arr, int target) {
        int count = 0;

        sort(arr.begin(), arr.end());

        for (int i = 0; i < arr.size(); i++) {
            const int firstNum = arr[i];

            vector<int>::const_iterator leftItr = arr.cbegin() + i + 1;
            vector<int>::const_iterator rightItr = arr.cend() - 1;

            while (leftItr < rightItr) {
                const int currentSum = firstNum + *leftItr + *rightItr;

                if (currentSum < target) {
                    count += rightItr - leftItr;
                    leftItr++;
                } else {
                    rightItr--;
                }
            }
        }

        return count;
    }
};

int main() {
    Solution sol;

    assert(sol.searchTriplets(vector<int>{-2, 0, 1, 3}, 2) == 2);
    assert(sol.searchTriplets(vector<int>{-1, 4, 2, 1, 3}, 5) == 4);
    assert(sol.searchTriplets(vector<int>{0, 0, 0, 0, 0}, 1) == 10);
    cout << "All test cases passed." << endl;

    return 0;
}
