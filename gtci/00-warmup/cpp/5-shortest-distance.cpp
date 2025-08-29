#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
   public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        int word1Idx = -1;
        int word2Idx = -1;

        int shortestDistance = words.size();

        for (int i = 0; i < words.size(); i++) {
            const string& word = words[i];
            if (word == word1) {
                word1Idx = i;

                if (word2Idx != -1)
                    shortestDistance =
                        min(abs(word1Idx - word2Idx), shortestDistance);
            }

            if (word == word2) {
                word2Idx = i;

                if (word1Idx != -1)
                    shortestDistance =
                        min(abs(word1Idx - word2Idx), shortestDistance);
            }

            if (shortestDistance == 1) return 1;
        }

        return shortestDistance;
    }
};

int main() {
    Solution sol;
    vector<string> words = {"the",  "quick", "brown", "fox", "jumps",
                            "over", "the",   "lazy",  "dog"};
    string word1 = "the";
    string word2 = "fox";
    cout << sol.shortestDistance(words, word1, word2) << endl;  // Output: 3

    vector<string> words2 = {"a", "c", "d", "b", "a"};
    string word3 = "a";
    string word4 = "b";
    cout << sol.shortestDistance(words2, word3, word4) << endl;  // Output: 1

    vector<string> words3 = {"a", "b", "c", "d", "e"};
    string word5 = "a";
    string word6 = "e";
    cout << sol.shortestDistance(words3, word5, word6) << endl;  // Output: 4

    return 0;
}
