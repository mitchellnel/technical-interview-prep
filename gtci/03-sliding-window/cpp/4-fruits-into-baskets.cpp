#include <algorithm>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
   public:
    int findLength(const vector<char> &fruits) {
        int maxLength = 0;

        int windowStart = 0;
        std::unordered_map<char, int> basket;
        for (int windowEnd = 0; windowEnd < fruits.size(); windowEnd++) {
            basket[fruits[windowEnd]] += 1;

            if (basket.size() <= 2)
                maxLength = std::max(maxLength, windowEnd - windowStart + 1);

            while (basket.size() > 2) {
                basket[fruits[windowStart]] -= 1;
                if (basket[fruits[windowStart]] == 0)
                    basket.erase(fruits[windowStart]);

                windowStart++;
            }
        }

        return maxLength;
    }
};

int main() {
    Solution sol;

    assert(sol.findLength(vector<char>{'A', 'B', 'C', 'A', 'C'}) == 3);
    assert(sol.findLength(vector<char>{'A', 'B', 'C', 'B', 'B', 'C'}) == 5);
    assert(sol.findLength(vector<char>{'A', 'A', 'A', 'A'}) == 4);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
