#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    int removeTargetKey(vector<int>& arr, const int& key) {
        int nextNonKey = 0;

        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] != key) {
                arr[nextNonKey] = arr[i];
                nextNonKey++;
            }
        }

        return nextNonKey;
    }
};

#include <cassert>

int main() {
    Solution sol;
    std::vector<int> arr = {2, 3, 3, 6, 6, 7, 8, 9, 9};
    int new_length = sol.removeTargetKey(arr, 3);
    std::vector<int> expected1 = {2, 6, 6, 7, 8, 9, 9};
    assert(std::vector<int>(arr.begin(), arr.begin() + new_length) ==
           expected1);

    std::vector<int> arr2 = {2, 2, 2, 11};
    new_length = sol.removeTargetKey(arr2, 2);
    std::vector<int> expected2 = {11};
    assert(std::vector<int>(arr2.begin(), arr2.begin() + new_length) ==
           expected2);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
