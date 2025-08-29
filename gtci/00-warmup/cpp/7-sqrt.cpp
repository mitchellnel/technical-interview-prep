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

int main() {
    Solution sol;
    std::cout << sol.mySqrt(4) << std::endl;  // Output: 2
    std::cout << sol.mySqrt(8) << std::endl;  // Output: 2
    std::cout << sol.mySqrt(0) << std::endl;  // Output: 0
    std::cout << sol.mySqrt(1) << std::endl;  // Output: 1
}
