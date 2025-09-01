#include <cassert>
#include <iostream>
#include <string>

using namespace std;

class Solution {
   public:
    static bool compare(const string &str1, const string &str2) {
        int idx1 = str1.size() - 1;
        int idx2 = str2.size() - 1;

        while (idx1 >= 0 || idx2 >= 0) {
            idx1 = Solution::getNextValidIndex(str1, idx1);
            idx2 = Solution::getNextValidIndex(str2, idx2);

            if (idx1 >= 0 && idx2 >= 0 && str1[idx1] != str2[idx2]) {
                return false;
            }

            idx1--;
            idx2--;
        }

        return idx1 == idx2;
    }

   private:
    static int getNextValidIndex(const string &str, int idx) {
        int backspaceCount = 0;

        while (idx >= 0) {
            if (str[idx] == '#') {
                backspaceCount++;
            } else if (backspaceCount > 0) {
                backspaceCount--;
            } else {
                return idx;
            }

            idx--;
        }

        return idx;
    }
};

int main() {
    Solution sol;

    assert(sol.compare("xy#z", "xzz#") == true);
    assert(sol.compare("xy#z", "xyz#") == false);
    assert(sol.compare("xp#", "xyz##") == true);
    cout << "All test cases passed." << endl;

    return 0;
}
