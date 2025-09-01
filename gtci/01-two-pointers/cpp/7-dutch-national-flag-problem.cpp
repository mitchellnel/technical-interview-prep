#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> sort(vector<int> &&arr) {
        std::vector<int>::iterator lowItr = arr.begin();
        std::vector<int>::iterator highItr = arr.end() - 1;

        std::vector<int>::iterator itr = arr.begin();
        while (itr <= highItr) {
            if (*itr == 0) {
                std::swap(*itr, *lowItr);
                lowItr++;
                itr++;
            } else if (*itr == 1) {
                itr++;
            } else {
                std::swap(*itr, *highItr);
                highItr--;
            }
        }

        return arr;
    }
};

int main() {
    Solution sol;

    assert(sol.sort(vector<int>{0, 1, 2, 0, 1, 2}) ==
           vector<int>({0, 0, 1, 1, 2, 2}));
    assert(sol.sort(vector<int>{2, 2, 0, 1, 2, 0}) ==
           vector<int>({0, 0, 1, 2, 2, 2}));
    cout << "All test cases passed." << endl;

    return 0;
}
