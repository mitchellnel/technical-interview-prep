#include <algorithm>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
   public:
    int largestUniqueNumber(vector<int>&& A) {
        std::unordered_map<int, int> freqMap;

        for (int num : A) freqMap[num] += 1;

        int maxUnique = -1;
        for (int num : A) {
            if (freqMap[num] == 1) maxUnique = std::max(maxUnique, num);
        }

        return maxUnique;
    }
};

int main() {
    Solution sol;

    assert(sol.largestUniqueNumber({5, 7, 3, 9, 4, 9, 8, 3, 2, 5}) == 8);
    assert(sol.largestUniqueNumber({1, 2, 3, 4, 5}) == 5);
    assert(sol.largestUniqueNumber({1, 1, 1, 1}) == -1);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
