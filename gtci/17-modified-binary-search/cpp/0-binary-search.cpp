#include <cassert>
#include <iostream>
#include <vector>

class Solution {
    public:
    int binarySearch(const std::vector<int>& nums, const int& target) {
        if (nums.empty())
            return -1;
        
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            const int mid = left + (right - left) / 2;    // avoid potential overflow

            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                left = mid + 1;
            else if (nums[mid] > target)
                right = mid - 1;
        }

        return -1;
    }
};

int main() {
    Solution s;

    assert(s.binarySearch({1,2,3,4,5}, 3) == 2);
    assert(s.binarySearch({1,2,3,4,5}, 1) == 0);
    assert(s.binarySearch({1,2,3,4,5}, 5) == 4);
    assert(s.binarySearch({1,2,3,4,5}, 6) == -1);
    assert(s.binarySearch({}, 1) == -1);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
