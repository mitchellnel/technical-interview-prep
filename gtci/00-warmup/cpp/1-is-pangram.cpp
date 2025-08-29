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

int main() {
    Solution sol;
    string sentence = "The quick brown fox jumps over the lazy dog";
    cout << (sol.checkIfPangram(sentence) ? "true" : "false")
         << endl;  // Output: true
    sentence = "Hello, World!";
    cout << (sol.checkIfPangram(sentence) ? "true" : "false")
         << endl;  // Output: false
    sentence = "abcdefghijklmnopqrstuvwxyz";
    cout << (sol.checkIfPangram(sentence) ? "true" : "false")
         << endl;  // Output: true
    return 0;
}
