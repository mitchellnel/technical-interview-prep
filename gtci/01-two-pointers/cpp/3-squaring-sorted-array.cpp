#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    static vector<int> makeSquares(const vector<int>& arr) {
        int n = arr.size();
        vector<int> squares(n);

        std::vector<int>::iterator squaresItr = squares.end() - 1;

        std::vector<int>::const_iterator left = arr.begin();
        std::vector<int>::const_iterator right = arr.end() - 1;

        while (left <= right) {
            if (abs(*left) > abs(*right)) {
                *squaresItr = *left * *left;
                squaresItr--;
                left++;
            } else if (abs(*right) >= abs(*left)) {
                *squaresItr = *right * *right;
                squaresItr--;
                right--;
            }
        }

        return squares;
    }
};

int main() {
    Solution sol;
    std::vector<int> arr = {-2, -1, 0, 1, 2};
    std::vector<int> result = sol.makeSquares(arr);
    std::vector<int> expected1 = {0, 1, 1, 4, 4};
    assert(result == expected1);

    std::vector<int> arr2 = {-3, -2, -1, 0, 1, 2, 3, 3};
    std::vector<int> result2 = sol.makeSquares(arr2);
    std::vector<int> expected2 = {0, 1, 1, 4, 4, 9, 9, 9};
    assert(result2 == expected2);

    std::vector<int> arr3 = {-3, -2, -1};
    std::vector<int> result3 = sol.makeSquares(arr3);
    std::vector<int> expected3 = {1, 4, 9};
    assert(result3 == expected3);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
