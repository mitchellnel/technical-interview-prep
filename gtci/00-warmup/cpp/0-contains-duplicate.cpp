#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

#include <cassert>

class Solution {
   public:
    bool containsDuplicate(vector<int> &nums) {
        unordered_set<int> appears{};
        for (int num : nums) {
            auto [_, inserted] = appears.insert(num);
            if (!inserted) return true;
        }
        return false;
    }
};

int main() {
    Solution sol;
    std::vector<int> test1 = {1, 2, 3, 1};
    std::vector<int> test2 = {1, 2, 3, 4};
    std::vector<int> test3 = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
    assert(sol.containsDuplicate(test1) == true);
    assert(sol.containsDuplicate(test2) == false);
    assert(sol.containsDuplicate(test3) == true);
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
