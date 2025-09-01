#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> findWordConcatenation(const string &str,
                                      const vector<string> &words) {
        vector<int> resultIndices;

        int wordLength = words[0].size();

        int windowStart = 0;
        int windowEnd = words.size() * wordLength - 1;
        while (windowEnd < str.size()) {
            std::unordered_map<std::string, bool> words_seen;
            for (std::string word : words) words_seen[word] = false;

            int nextWordIndex = windowStart;
            while (nextWordIndex <= windowEnd) {
                const std::string word = str.substr(nextWordIndex, wordLength);

                if (words_seen.find(word) == words_seen.end()) break;

                words_seen[word] = true;

                if (std::all_of(words_seen.begin(), words_seen.end(),
                                [](const auto &p) { return p.second; })) {
                    resultIndices.push_back(windowStart);
                }

                nextWordIndex += wordLength;
            }

            windowStart++;
            windowEnd = windowStart + words.size() * wordLength - 1;
        }

        return resultIndices;
    }
};

int main() {
    Solution sol;

    assert(sol.findWordConcatenation("catfoxcat", {"cat", "fox"}) ==
           vector<int>({0, 3}));
    assert(sol.findWordConcatenation("catcatfoxfox", {"cat", "fox"}) ==
           vector<int>({3}));
    assert(sol.findWordConcatenation("horsedogcat", {"cat", "dog"}) ==
           vector<int>({5}));

    cout << "All test cases passed." << endl;
    return 0;
}