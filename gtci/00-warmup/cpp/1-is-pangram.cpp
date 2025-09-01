#include <cctype>
#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
   public:
    bool checkIfPangram(string sentence) {
        unordered_set<char> letters{};

        for (char ch : sentence) {
            if (!isalpha(ch)) continue;

            if (letters.find(tolower(ch)) ==
                letters.end())  // contains is a > C++20 feature
                letters.insert(tolower(ch));
        }

        return letters.size() == 26;
    }
};

#include <cassert>

int main() {
    Solution sol;
    assert(sol.checkIfPangram("The quick brown fox jumps over the lazy dog") ==
           true);
    assert(sol.checkIfPangram("Hello, World!") == false);
    assert(sol.checkIfPangram("abcdefghijklmnopqrstuvwxyz") == true);
    assert(sol.checkIfPangram("You shall not pass!") == false);
    assert(sol.checkIfPangram("Pack my box with five dozen liquor jugs.") ==
           true);
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
