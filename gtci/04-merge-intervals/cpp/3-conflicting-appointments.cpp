#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

#include "interval.h"

using namespace std;

class Solution {
   public:
    bool canAttendAllAppointments(vector<Interval>& intervals) {
        if (intervals.size() < 2) return true;

        std::sort(intervals.begin(), intervals.end(),
                  [](Interval a, Interval b) { return a.start < b.start; });

        for (size_t i = 1; i < intervals.size(); i++) {
            Interval& first = intervals[i - 1];
            Interval& second = intervals[i];

            if (second.start < first.end) return false;
        }

        return true;
    }
};

int main() {
    Solution sol;

    vector<Interval> intervals1 = {Interval(1, 4), Interval(2, 5),
                                   Interval(7, 9)};
    assert(!sol.canAttendAllAppointments(intervals1));

    vector<Interval> intervals2 = {
        Interval(6, 7),  Interval(2, 4),   Interval(13, 14),
        Interval(8, 12), Interval(45, 47),
    };
    assert(sol.canAttendAllAppointments(intervals2));

    vector<Interval> intervals3 = {Interval(4, 5), Interval(2, 3),
                                   Interval(3, 6)};
    assert(!sol.canAttendAllAppointments(intervals3));

    cout << "All test cases passed." << endl;

    return 0;
}
