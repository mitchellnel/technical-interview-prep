#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    static vector<int> search(const vector<int> &arr, int targetSum) {
        int left = 0;
        int right = arr.size() - 1;

        while (left < right) {
            const int sum = arr[left] + arr[right];

            if (sum < targetSum)
                left++;
            else if (sum > targetSum)
                right--;
            else
                return std::vector<int>{left, right};
        }

        return vector<int>(2, -1);
    }
};

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 6};
    int targetSum = 6;
    std::vector<int> result = Solution::search(arr, targetSum);
    assert(result == std::vector<int>({1, 3}));

    std::vector<int> arr2 = {2, 5, 9, 11};
    int targetSum2 = 11;
    std::vector<int> result2 = Solution::search(arr2, targetSum2);
    assert(result2 == std::vector<int>({0, 2}));

    std::vector<int> arr3 = {1, 3, 5, 7};
    int targetSum3 = 8;
    std::vector<int> result3 = Solution::search(arr3, targetSum3);
    assert(result3 == std::vector<int>({0, 3}));

    std::vector<int> arr4 = {1, 2, 3, 4, 5};
    int targetSum4 = 10;
    std::vector<int> result4 = Solution::search(arr4, targetSum4);
    assert(result4 == std::vector<int>({-1, -1}));

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
