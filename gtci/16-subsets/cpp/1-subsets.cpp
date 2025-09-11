#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> findSubsets(const vector<int>& nums) {
    vector<vector<int>> subsets {{}};
    
    for (int num : nums) {
      const size_t nSubsets = subsets.size();
      for (size_t i = 0; i < nSubsets; i++) {
        vector<int> newSubset = subsets[i];
        newSubset.push_back(num);

        subsets.push_back(newSubset);
      }
    }

    return subsets;
  }
};    

int main() {
    Solution s;
    
    vector<vector<int>> result1 = s.findSubsets({1,2,3});
    assert(result1.size() == 8);
    assert(result1[0] == vector<int>({}));
    assert(result1[1] == vector<int>({1}));
    assert(result1[2] == vector<int>({2}));
    assert(result1[3] == vector<int>({1,2}));
    assert(result1[4] == vector<int>({3}));
    assert(result1[5] == vector<int>({1,3}));
    assert(result1[6] == vector<int>({2,3}));
    assert(result1[7] == vector<int>({1,2,3}));
    
    vector<vector<int>> result2 = s.findSubsets({0});
    assert(result2.size() == 2);
    assert(result2[0] == vector<int>({}));
    assert(result2[1] == vector<int>({0}));

    std::cout << "All test cases passed." << std::endl;
    
    return 0;
}
