#include <cassert>
#include <iostream>
#include <stack>

class Solution {
   public:
    std::string removeDuplicates(std::string s) {
        std::stack<char> charStack;

        for (char ch : s) {
            if (charStack.size() > 0 && ch == charStack.top())
                charStack.pop();
            else
                charStack.push(ch);
        }

        std::string result = "";
        while (charStack.size() > 0) {
            result = charStack.top() + result;
            charStack.pop();
        }

        return result;
    }
};

int main() {
    Solution sol = Solution();

    assert(sol.removeDuplicates("abccba") == "");
    assert(sol.removeDuplicates("foobar") == "fbar");
    assert(sol.removeDuplicates("fooobar") == "fobar");
    assert(sol.removeDuplicates("abcd") == "abcd");

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
