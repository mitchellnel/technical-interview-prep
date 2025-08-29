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

int main() {
    Solution solution;
    std::string testString = "A man, a plan, a canal: Panama";
    if (solution.isPalindrome(testString)) {
        std::cout << "\"" << testString << "\" is a palindrome." << std::endl;
    } else {
        std::cout << "\"" << testString << "\" is not a palindrome."
                  << std::endl;
    }

    std::string anotherTestString = "Was it a car or a cat I saw?";
    if (solution.isPalindrome(anotherTestString)) {
        std::cout << "\"" << anotherTestString << "\" is a palindrome."
                  << std::endl;
    } else {
        std::cout << "\"" << anotherTestString << "\" is not a palindrome."
                  << std::endl;
    }

    return 0;
}
