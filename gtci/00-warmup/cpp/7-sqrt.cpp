#include <iostream>

class Solution {
   public:
    int mySqrt(int x) {
        if (x < 2) return x;

        int left = 2;
        int right = x / 2;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            long long num = (long long)mid * mid;

            if (num < x) {
                left = mid + 1;
            } else if (num > x) {
                right = mid - 1;
            } else {
                return mid;
            }
        }

        return right;
    }
};

#include <cassert>

int main() {
    Solution sol;
    assert(sol.mySqrt(4) == 2);
    assert(sol.mySqrt(8) == 2);
    assert(sol.mySqrt(0) == 0);
    assert(sol.mySqrt(1) == 1);
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
