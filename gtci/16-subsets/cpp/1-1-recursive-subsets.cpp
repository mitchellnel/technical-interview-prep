#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> findSubsets(const vector<int>& nums) {
    vector<vector<int>> subsets {};

    backtrack(nums, subsets, 0, {});

    return subsets;
  }

  void backtrack(const vector<int>& nums, vector<vector<int>>& subsets, size_t start, vector<int> path) {
    subsets.push_back(vector<int>(path));

    for (size_t i = start; i < nums.size(); i++) {
      path.push_back(nums[i]);
      backtrack(nums, subsets, i + 1, path);
      path.pop_back();
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
    {}, {1}, {2}, {1,2}, {3}, {1,3}, {2,3}, {1,2,3}
  };
  vector<vector<int>> result1 = s.findSubsets({1,2,3});
  assert(result1.size() == expected1.size());
  for (const auto& subset : expected1) {
    assert(contains(result1, subset));
  }

  vector<vector<int>> expected2 = {
    {}, {0}
  };
  vector<vector<int>> result2 = s.findSubsets({0});
  assert(result2.size() == expected2.size());
  for (const auto& subset : expected2) {
    assert(contains(result2, subset));
  }

  std::cout << "All test cases passed." << std::endl;
  return 0;
}
