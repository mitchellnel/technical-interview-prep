#include <cctype>
#include <iostream>
#include <string>
#include <unordered_set>

class Solution {
   public:
    std::string reverseVowels(std::string s) {
        const std::unordered_set<char> vowels{'a', 'e', 'i', 'o', 'u'};

        std::string::iterator left = s.begin();
        std::string::iterator right = s.end() - 1;

        while (left < right) {
            if (vowels.find(tolower(*left)) == vowels.end()) left += 1;

            if (vowels.find(tolower(*right)) == vowels.end()) right -= 1;

            if (vowels.find(tolower(*left)) != vowels.end() &&
                vowels.find(tolower(*right)) != vowels.end()) {
                std::swap(*left, *right);

                left += 1;
                right -= 1;
            }
        }

        return s;
    }
};

int main() {
    Solution sol;
    std::string s = "hello";
    std::cout << sol.reverseVowels(s) << std::endl;  // Output: "holle"
    s = "AEIOUD";
    std::cout << sol.reverseVowels(s) << std::endl;  // Output: "UOIEA"
    s = "DesignGUrus";
    std::cout << sol.reverseVowels(s) << std::endl;  // Output: "DusUgnGires"
    return 0;
}
