#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#include <cassert>

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
    std::vector<std::string> words = {"the",  "quick", "brown", "fox", "jumps",
                                      "over", "the",   "lazy",  "dog"};
    assert(sol.shortestDistance(words, "the", "fox") == 3);
    std::vector<std::string> words2 = {"a", "c", "d", "b", "a"};
    assert(sol.shortestDistance(words2, "a", "b") == 1);
    std::vector<std::string> words3 = {"a", "b", "c", "d", "e"};
    assert(sol.shortestDistance(words3, "a", "e") == 4);
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
