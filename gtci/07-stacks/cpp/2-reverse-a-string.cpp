#include <cassert>
#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
   public:
    string reverseString(string s) {
        std::stack<char> stack;

        for (char ch : s) stack.push(ch);

        std::string reversedStr;
        while (stack.size() > 0) {
            reversedStr += stack.top();
            stack.pop();
        }

        return reversedStr;
    }
};

int main() {
    Solution sol;

    assert(sol.reverseString("hello") == "olleh");
    assert(sol.reverseString("world") == "dlrow");
    assert(sol.reverseString("Python") == "nohtyP");

    cout << "All test cases passed." << endl;

    return 0;
}
