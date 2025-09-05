#include <algorithm>
#include <cassert>
#include <iostream>
#include <stack>
#include <utility>

using namespace std;

class Solution {
   public:
    string removeDuplicates(string s, int k) {
        std::stack<std::pair<char, int>> stack;

        for (char ch : s) {
            if (!stack.empty() && ch == stack.top().first &&
                k - 1 == stack.top().second)
                stack.pop();
            else if (!stack.empty() && ch == stack.top().first)
                stack.top().second++;
            else
                stack.push({ch, 1});
        }

        std::string result;
        while (!stack.empty()) {
            result.append(stack.top().second, stack.top().first);
            stack.pop();
        }

        std::reverse(result.begin(), result.end());

        return result;
    }
};

int main() {
    Solution sol;

    assert(sol.removeDuplicates("abbbaaca", 3) == "ca");
    assert(sol.removeDuplicates("abbaccaa", 3) == "abbaccaa");
    assert(sol.removeDuplicates("abbacccaa", 3) == "abb");

    cout << "All test cases passed." << endl;
    return 0;
}
