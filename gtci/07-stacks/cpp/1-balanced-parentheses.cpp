#include <cassert>
#include <iostream>
#include <stack>

using namespace std;

class Solution {
   public:
    bool isValid(string s) {
        std::stack<char> stack;

        for (char ch : s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else {
                if (stack.size() == 0) return false;

                const char top = stack.top();
                stack.pop();

                if (ch == ')' && top != '(')
                    return false;
                else if (ch == ']' && top != '[')
                    return false;
                else if (ch == '}' && top != '{')
                    return false;
            }
        }

        return stack.size() == 0;
    }
};

int main() {
    Solution sol;

    assert(sol.isValid("()") == true);
    assert(sol.isValid("()[]{}") == true);
    assert(sol.isValid("(]") == false);
    assert(sol.isValid("([)]") == false);
    assert(sol.isValid("{[]}") == true);
    assert(sol.isValid("}") == false);

    cout << "All test cases passed." << endl;

    return 0;
}
