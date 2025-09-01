#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    int moveElements(vector<int> &arr) {
        int nextNonDuplicate = 1;

        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] != arr[nextNonDuplicate - 1]) {
                arr[nextNonDuplicate] = arr[i];
                nextNonDuplicate++;
            }
        }

        return nextNonDuplicate;
    }
};

int main() {
    Solution sol;

    std::vector<int> arr = {2, 3, 3, 6, 6, 7, 8, 9, 9};
    int new_length = sol.moveElements(arr);
    std::vector<int> expected1 = {2, 3, 6, 7, 8, 9};
    assert(std::vector<int>(arr.begin(), arr.begin() + new_length) ==
           expected1);

    std::vector<int> arr2 = {2, 2, 2, 11};
    new_length = sol.moveElements(arr2);
    std::vector<int> expected2 = {2, 11};
    assert(std::vector<int>(arr2.begin(), arr2.begin() + new_length) ==
           expected2);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
