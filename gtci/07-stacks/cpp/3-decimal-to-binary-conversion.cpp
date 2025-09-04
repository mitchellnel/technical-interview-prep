#include <cassert>
#include <iostream>
#include <stack>

using namespace std;

class Solution {
   public:
    string decimalToBinary(int num) {
        if (num == 0) return "0";

        std::stack<int> stack;

        while (num != 0) {
            stack.push(num % 2);
            num /= 2;
        }

        std::string binary;
        while (stack.size() > 0) {
            binary += std::to_string(stack.top());
            stack.pop();
        }

        return binary;
    }
};

int main() {
    Solution sol;

    assert(sol.decimalToBinary(0) == "0");
    assert(sol.decimalToBinary(5) == "101");
    assert(sol.decimalToBinary(10) == "1010");
    assert(sol.decimalToBinary(255) == "11111111");

    cout << "All test cases passed." << endl;

    return 0;
}
