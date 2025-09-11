#include <cassert>
#include <cctype>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

const std::unordered_set<char> OPERATORS { '+', '-', '*' };

class Solution {
public:
  std::vector<int> diffWaysToEvaluateExpression(const std::string& input) {
    std::unordered_map<std::string, std::vector<int>> memo;
    return dfs(input, memo);
  }
private:
  std::vector<int> dfs(const std::string& expr, std::unordered_map<std::string, std::vector<int>> memo) {
    // base case -- memoised expression
    if (memo.contains(expr))
      return memo[expr];
    
    // base case -- no operators
    if (noOperatorsInExpression(expr))
      return { std::stoi(expr) };

    std::vector<int> results;
    
    // find operator breakpoints
    for (size_t i = 0; i < expr.size(); i++) {
      const char ch = expr[i];

      if (OPERATORS.contains(ch)) {
        const std::vector<int> left_values = dfs(
          expr.substr(0, i),
          memo
        );

        const std::vector<int> right_values = dfs(
          expr.substr(i + 1, expr.size()),
          memo
        );

        for (int lhs : left_values) {
          for (int rhs : right_values) {
            if (ch == '+') {
              results.push_back(lhs + rhs);
            } else if (ch == '-') {
              results.push_back(lhs - rhs);
            } else if (ch == '*') {
              results.push_back(lhs * rhs);
            }
          }
        }
      }
    }

    memo[expr] = results;
    return results;
  }

  bool noOperatorsInExpression(const std::string& expr) {
    for (size_t i = 0; i < expr.size(); i++) {
      if (OPERATORS.contains(expr[i]))
        return false;
    }

    return true;
  }
};

int main() {
    Solution sol;

    const std::vector<int> result1 = sol.diffWaysToEvaluateExpression("1+2*3");
    assert(std::is_permutation(
        result1.begin(),
        result1.end(),
        std::vector<int> {7, 9}.begin()
    ));

    const std::vector<int> result2 = sol.diffWaysToEvaluateExpression("2*3-4*5");
    assert(std::is_permutation(
        result2.begin(),
        result2.end(),
        std::vector<int> {-34, -14, -10, -10, 10}.begin()
    ));

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
