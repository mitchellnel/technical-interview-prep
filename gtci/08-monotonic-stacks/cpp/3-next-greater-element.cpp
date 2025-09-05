#include <cassert>
#include <iostream>
#include <stack>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> nextGreaterElement(vector<int>&& nums1, vector<int>&& nums2) {
        std::unordered_map<int, int> nextGreaterElementMap;
        std::stack<int> stack;

        for (int i = nums2.size() - 1; i >= 0; i--) {
            while (stack.size() > 0 && nums2[i] > stack.top()) stack.pop();

            nextGreaterElementMap[nums2[i]] =
                stack.size() > 0 ? stack.top() : -1;
            stack.push(nums2[i]);
        }

        std::vector<int> result;
        for (int num : nums1) {
            if (nextGreaterElementMap.contains(num))
                result.push_back(nextGreaterElementMap[num]);
        }

        return result;
    }
};

int main() {
    Solution sol = Solution();

    assert(sol.nextGreaterElement({4, 2, 6}, {6, 2, 4, 5, 3, 7}) ==
           vector<int>({5, 4, 7}));
    assert(sol.nextGreaterElement({9, 7, 1}, {1, 7, 9, 5, 4, 3}) ==
           vector<int>({-1, 9, 7}));
    assert(sol.nextGreaterElement({5, 12, 3}, {12, 3, 5, 4, 10, 15}) ==
           vector<int>({10, 15, 5}));

    cout << "All test cases passed." << endl;

    return 0;
}
