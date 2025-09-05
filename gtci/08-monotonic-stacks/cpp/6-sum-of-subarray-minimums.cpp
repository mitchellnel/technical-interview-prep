#include <cassert>
#include <cmath>
#include <iostream>
#include <stack>
#include <vector>

class Solution {
   public:
    int sumSubarrayMins(std::vector<int>&& arr) {
        const int MOD = std::pow(10, 9) + 7;

        int result = 0;
        std::stack<int> stack;

        for (int i = 0; i < arr.size() + 1; i++) {
            int curr = i < arr.size() ? arr[i] : 0;

            while (!stack.empty() && curr < arr[stack.top()]) {
                int minIndex = stack.top();
                stack.pop();

                int previousIndex = !stack.empty() ? stack.top() : -1;

                int subarrayCount = (minIndex - previousIndex) * (i - minIndex);

                result = (result + (arr[minIndex] * subarrayCount) % MOD) % MOD;
            }

            stack.push(i);
        }

        return result;
    }
};

int main() {
    Solution sol;

    assert(sol.sumSubarrayMins({3, 1, 2, 4}) == 17);
    assert(sol.sumSubarrayMins({5, 4, 3, 2, 1}) == 35);
    assert(sol.sumSubarrayMins({3, 1, 2, 4, 5}) == 30);
    assert(sol.sumSubarrayMins({2, 6, 5, 4}) == 36);
    assert(sol.sumSubarrayMins({7, 3, 8}) == 27);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
