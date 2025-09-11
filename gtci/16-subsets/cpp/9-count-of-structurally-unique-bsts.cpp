#include <cassert>
#include <iostream>
#include <unordered_map>

class Solution {
public:
  int countTrees(int n) {
    if (memo.contains(n))
      return memo[n];

    if (n <= 1)
      return 1;
    
    int count = 0;

    for (int rootVal = 1; rootVal < n + 1; rootVal++) {
      int leftSubtreeCount = countTrees(rootVal - 1);
      int rightSubtreeCount = countTrees(n - rootVal);

      count += leftSubtreeCount * rightSubtreeCount;
    }

    memo[n] = count;
    return count;
  }
private:
  std::unordered_map<int, int> memo;
};

int main() {
  Solution s;

  assert(s.countTrees(2) == 2);
  assert(s.countTrees(3) == 5);

  std::cout << "All test cases passed." << std::endl;
  return 0;
}