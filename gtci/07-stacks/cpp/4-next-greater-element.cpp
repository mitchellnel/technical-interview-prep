#include <cassert>
#include <iostream>
#include <stack>
#include <vector>

class Solution {
   public:
    std::vector<int> nextLargerElement(std::vector<int> arr) {
        std::vector<int> res(arr.size(), -1);

        std::stack<int> stack;

        for (int i = arr.size() - 1; i >= 0; i--) {
            int num = arr[i];

            while (stack.size() > 0 && stack.top() <= num) stack.pop();

            if (stack.size() != 0) res[i] = stack.top();

            stack.push(num);
        }

        return res;
    }
};

int main() {
    Solution sol;

    assert(sol.nextLargerElement({4, 5, 2, 10, 8}) ==
           std::vector<int>({5, 10, 10, -1, -1}));
    assert(sol.nextLargerElement({4, 5, 2, 25}) ==
           std::vector<int>({5, 25, 25, -1}));
    assert(sol.nextLargerElement({13, 7, 6, 12}) ==
           std::vector<int>({-1, 12, 12, -1}));
    assert(sol.nextLargerElement({1, 2, 3, 4, 5}) ==
           std::vector<int>({2, 3, 4, 5, -1}));
    assert(sol.nextLargerElement({3, 2, 1}) == std::vector<int>({-1, -1, -1}));
    assert(sol.nextLargerElement({1, 2, 3}) == std::vector<int>({2, 3, -1}));

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
