#include <cassert>
#include <iostream>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
   public:
    static vector<int> findNumbers(vector<int>&& nums, int k) {
        vector<int> missingNumbers;

        size_t i = 0;
        while (i < nums.size()) {
            int correctPosition = nums[i] - 1;

            if (correctPosition < nums.size() && nums[i] >= 1 &&
                nums[i] != nums[correctPosition]) {
                std::swap(nums[i], nums[correctPosition]);
            } else {
                i++;
            }
        }

        std::unordered_set<int> extraNumbers;
        for (i = 0; i < nums.size(); i++) {
            if (i + 1 != nums[i]) {
                missingNumbers.push_back(i + 1);

                if (missingNumbers.size() == k) return missingNumbers;

                extraNumbers.insert(nums[i]);
            }
        }

        i = 1;
        while (missingNumbers.size() < k) {
            const int candidate_number = static_cast<int>(i) + nums.size();

            if (!extraNumbers.contains(candidate_number))
                missingNumbers.push_back(candidate_number);

            i++;
        }

        return missingNumbers;
    }
};

int main() {
    Solution sol;

    assert(sol.findNumbers({3, -1, 4, 5, 5}, 3) == vector<int>({1, 2, 6}));
    assert(sol.findNumbers({2, 3, 4}, 3) == vector<int>({1, 5, 6}));
    assert(sol.findNumbers({-2, -3, 4}, 2) == vector<int>({1, 2}));

    cout << "All test cases passed." << endl;

    return 0;
}
