#include <cassert>
#include <iostream>
#include <stack>

class Solution {
   public:
    static std::stack<int> sortStack(std::stack<int> &input) {
        if (input.size() < 2) return input;

        std::stack<int> sortedStack;

        while (input.size() > 0) {
            int top = input.top();
            input.pop();

            while (sortedStack.size() > 0 && sortedStack.top() > top) {
                input.push(sortedStack.top());
                sortedStack.pop();
            }

            sortedStack.push(top);
        }

        return sortedStack;
    }
};

int main() {
    Solution sol;

    std::stack<int> s1;
    s1.push(34);
    s1.push(3);
    s1.push(31);
    s1.push(98);
    s1.push(92);
    s1.push(23);
    assert(sol.sortStack(s1) == std::stack<int>({3, 23, 31, 34, 92, 98}));

    std::stack<int> s2;
    s2.push(4);
    s2.push(3);
    s2.push(2);
    s2.push(10);
    s2.push(12);
    s2.push(1);
    s2.push(5);
    s2.push(6);
    assert(sol.sortStack(s2) == std::stack<int>({1, 2, 3, 4, 5, 6, 10, 12}));

    std::stack<int> s3;
    s3.push(20);
    s3.push(10);
    s3.push(-5);
    s3.push(-1);
    assert(sol.sortStack(s3) == std::stack<int>({-5, -1, 10, 20}));

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
