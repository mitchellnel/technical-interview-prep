#include <cassert>
#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
  std::vector<std::string> generateValidParentheses(int num) {
    std::vector<std::string> result;
    backtrack(result, num * 2, 0, 0, "");
    return result;
  }
private:
  void backtrack(std::vector<std::string>& result, const int maxParens, const int totalParenCount, const int openParenCount, const std::string path) {
    // base case
    if (totalParenCount == maxParens) {
      result.push_back(path);
      return;
    }

    // at every step we have two choices:
    // - open a parentheses block
    // - close a parentheses if we've one open already
    if (openParenCount > 0)
      backtrack(result, maxParens, totalParenCount + 1, openParenCount - 1, path + ")");
    
    if (totalParenCount + openParenCount < maxParens) {
      backtrack(result, maxParens, totalParenCount + 1, openParenCount + 1, path + "(");
    }
  }
};

int main() {
    Solution s;
    
    auto contains = [](const std::vector<std::string>& result, const std::string& subset) {
        for (const auto& s : result) {
        if (s == subset) return true;
        }
        return false;
    };
    
    std::vector<std::string> expected1 = {
        "()()()", "((()))", "(())()", "(()())", "()(())"
    };
    std::vector<std::string> result1 = s.generateValidParentheses(3);
    assert(result1.size() == expected1.size());
    for (const auto& subset : expected1) {
        assert(contains(result1, subset));
    }
    
    std::vector<std::string> expected2 = {
        "()()", "(())"
    };
    std::vector<std::string> result2 = s.generateValidParentheses(2);
    assert(result2.size() == expected2.size());
    for (const auto& subset : expected2) {
        assert(contains(result2, subset));
    }
    
    std::cout << "All test cases passed." << std::endl;

    return 0;
}
