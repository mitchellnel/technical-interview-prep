#include <cctype>
#include <iostream>

class Solution {
   public:
    bool isPalindrome(std::string s) {
        std::string::iterator left = s.begin();
        std::string::iterator right = s.end();

        while (left < right) {
            while (left < right && !isalnum(*left)) left++;

            while (left < right && !isalnum(*right)) right--;

            if (tolower(*left) != tolower(*right)) return false;

            left++;
            right--;
        }

        return true;
    }
};

#include <cassert>

int main() {
    Solution solution;
    assert(solution.isPalindrome("A man, a plan, a canal: Panama") == true);
    assert(solution.isPalindrome("Was it a car or a cat I saw?") == true);
    assert(solution.isPalindrome("race a car") == false);
    std::cout << "All test cases passed." << std::endl;

    return 0;
}
