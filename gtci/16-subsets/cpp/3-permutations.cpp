#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> findPermutations(const vector<int>& nums) {
    vector<vector<int>> permutations;

    const size_t n = nums.size();
    std::vector<bool> used (n, false);
    
    backtrack(nums, permutations, used, {});
    return permutations;
  }

private:
  void backtrack(const vector<int>& nums, std::vector<std::vector<int>>& permutations, std::vector<bool>& used, std::vector<int> path) {
    if (path.size() == nums.size()) {
      permutations.push_back(path);
    }

    for (size_t i = 0; i < nums.size(); i++) {
      if (used[i])
        continue;
      
      used[i] = true;
      path.push_back(nums[i]);
      backtrack(nums, permutations, used, path);
      path.pop_back();
      used[i] = false;
    }
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
