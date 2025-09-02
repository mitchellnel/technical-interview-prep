#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

#include "interval.h"
#include "util.h"

using namespace std;

class Solution {
   public:
    vector<Interval> merge(const vector<Interval> &arr1,
                           const vector<Interval> &arr2) {
        vector<Interval> result;

        auto itr1 = arr1.cbegin();
        auto itr2 = arr2.cbegin();

        while (itr1 < arr1.cend() && itr2 < arr2.cend()) {
            const int start = std::max(itr1->start, itr2->start);
            const int end = std::min(itr1->end, itr2->end);

            if (start <= end) {
                result.push_back(Interval(start, end));
            }

            if (itr1->end < itr2->end)
                itr1++;
            else
                itr2++;
        }

        return result;
    }
};

int main() {
    Solution sol;

    vector<Interval> result1 =
        sol.merge({Interval(1, 3), Interval(5, 6), Interval(7, 9)},
                  {Interval(2, 3), Interval(5, 7)});

    assert_equal_intervals(result1, vector<Interval>{{2, 3}, {5, 6}, {7, 7}});

    vector<Interval> result2 = sol.merge(
        {Interval(1, 3), Interval(5, 7), Interval(9, 12)}, {Interval(5, 10)});

    assert_equal_intervals(result2, vector<Interval>{{5, 7}, {9, 10}});

    cout << "All test cases passed.\n";

    return 0;
}