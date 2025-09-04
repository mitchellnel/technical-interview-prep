#include <cassert>
#include <iostream>
#include <sstream>
#include <stack>

class Solution {
   public:
    std::string simplifyPath(std::string path) {
        std::stack<std::string> stack;

        std::istringstream iss(path);
        std::string p;
        while (std::getline(iss, p, '/')) {
            if (p == "..") {
                if (stack.size() > 0) stack.pop();
            } else if (!p.empty() && p != ".") {
                stack.push(p);
            }
        }

        std::string result;
        while (!stack.empty()) {
            result = "/" + stack.top() + result;
            stack.pop();
        }

        return result.empty() ? "/" : result;
    }
};

int main() {
    Solution sol;

    assert(sol.simplifyPath("/home/") == "/home");
    assert(sol.simplifyPath("/../") == "/");
    assert(sol.simplifyPath("/home//foo/") == "/home/foo");
    assert(sol.simplifyPath("/a/./b/../../c/") == "/c");
    assert(sol.simplifyPath("/a//b////c/d//././/..") == "/a/b/c");

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
