#include <algorithm>
#include <cassert>
#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
   public:
    string removeKdigits(string num, int k) {
        std::stack<int> stack;

        int removed = 0;
        for (char digit : num) {
            while (!stack.empty() && removed < k &&
                   (digit - '0') < stack.top()) {
                stack.pop();
                removed++;
            }

            stack.push(digit - '0');
        }

        while (removed < k) {
            stack.pop();
            removed++;
        }

        std::string result;
        while (!stack.empty()) {
            result += std::to_string(stack.top());
            stack.pop();
        }

        std::reverse(result.begin(), result.end());

        result.erase(0, result.find_first_not_of('0'));

        return result != "" ? result : "0";
    }
};

int main() {
    Solution sol;

    assert(sol.removeKdigits("1432219", 3) == "1219");
    assert(sol.removeKdigits("10200", 1) == "200");
    assert(sol.removeKdigits("10", 2) == "0");
    assert(sol.removeKdigits("1234567890", 9) == "0");
    assert(sol.removeKdigits("9876543210", 5) == "43210");

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
