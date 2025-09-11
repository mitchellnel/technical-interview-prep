#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> findSubsets(vector<int>& nums) {
    std::sort(nums.begin(), nums.end());

    vector<vector<int>> subsets {{}};
    size_t startIdx = 0;

    for (size_t i = 0; i < nums.size(); i++) {
      size_t s = 0;
      if (i > 0 && nums[i - 1] == nums[i])
        s = startIdx;
      
      size_t nSubsets = subsets.size();
      while (s < nSubsets) {
        vector<int> newSubset(subsets[s]);
        newSubset.push_back(nums[i]);

        subsets.push_back(newSubset);

        s++;
      }

      startIdx = s;
    }

    return subsets;
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
    vector<int> input1 = {1,2,3};
    vector<vector<int>> result1 = s.findSubsets(input1);
    assert(result1.size() == expected1.size());
    for (const auto& subset : expected1) {
        assert(contains(result1, subset));
    }
    
    vector<vector<int>> expected2 = {
        {}, {0}
    };
    vector<int> input2 = {0};
    vector<vector<int>> result2 = s.findSubsets(input2);
    assert(result2.size() == expected2.size());
    for (const auto& subset : expected2) {
        assert(contains(result2, subset));
    }
    
    vector<vector<int>> expected3 = {
        {}, {1}, {2}, {1,2}, {2,2}, {1,2,2}
    };
    vector<int> input3 = {1,2,2};
    vector<vector<int>> result3 = s.findSubsets(input3);
    assert(result3.size() == expected3.size());
    for (const auto& subset : expected3) {
        assert(contains(result3, subset));
    }
    
    std::cout << "All test cases passed." << std::endl;
    
    return 0;
}
