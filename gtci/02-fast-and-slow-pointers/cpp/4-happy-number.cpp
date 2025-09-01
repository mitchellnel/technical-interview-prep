#include <cassert>
#include <iostream>

using namespace std;

class Solution {
   public:
    bool find(int num) {
        int slow = num;
        int fast = num;

        do {
            slow = Solution::calculateSquareSum(slow);
            fast = Solution::calculateSquareSum(
                Solution::calculateSquareSum(fast));
        } while (slow != fast);

        return slow == 1;
    }

   private:
    static int calculateSquareSum(int num) {
        int squareSum = 0;

        while (num > 0) {
            const int digit = num % 10;
            squareSum += digit * digit;

            num /= 10;
        }

        return squareSum;
    }
};

int main() {
    Solution sol;
    assert(sol.find(23) == true);
    assert(sol.find(12) == false);

    cout << "All test cases passed." << endl;

    return 0;
}
