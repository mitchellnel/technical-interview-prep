#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> findPermutations(const vector<int>& nums) {
    std::queue<vector<int>> q;
    q.push({});

    for (int num: nums) {
      const size_t levelSize = q.size();
      for (size_t j = 0; j < levelSize; j++) {
        std::vector<int> permutation = q.front();
        q.pop();

        for (size_t i = 0; i < permutation.size() + 1; i++) {
          std::vector<int> newPermutation(permutation.begin(), permutation.begin() + i);
          newPermutation.push_back(num);
          newPermutation.insert(newPermutation.end(), permutation.begin() + i, permutation.end());

          q.push(newPermutation);
        }
      }
    }
    
    vector<vector<int>> permutations;
    while (!q.empty()) {
      permutations.push_back(q.front());
      q.pop();
    }
    return permutations;
  }
};


int main() {
    Solution s;
    
    auto contains = [](const vector<vector<int>>& result, const vector<int>& subset) {
        for (const auto& s : result) {
        if (s == subset) return true;
        }
        return false;
    };
    
    vector<vector<int>> expected1 = {
        {1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,1,2}, {3,2,1}
    };
    vector<vector<int>> result1 = s.findPermutations({1,2,3});
    assert(result1.size() == expected1.size());
    for (const auto& subset : expected1) {
        assert(contains(result1, subset));
    }
    
    vector<vector<int>> expected2 = {
        {0}
    };
    vector<vector<int>> result2 = s.findPermutations({0});
    assert(result2.size() == expected2.size());
    for (const auto& subset : expected2) {
        assert(contains(result2, subset));
    }
    
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
