#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

#include "interval.h"

using namespace std;

class Solution {
   public:
    vector<Interval> findEmployeeFreeTime(
        const vector<vector<Interval>> &schedule) {
        vector<Interval> result;

        auto employeeCompare = [](const pair<Interval, pair<int, int>> &x,
                                  const pair<Interval, pair<int, int>> &y) {
            return x.first.start > y.first.start;
        };

        std::priority_queue<std::pair<Interval, std::pair<int, int>>,
                            vector<std::pair<Interval, std::pair<int, int>>>,
                            decltype(employeeCompare)>
            minHeap(employeeCompare);

        for (size_t i = 0; i < schedule.size(); i++) {
            const vector<Interval> &curr = schedule[i];
            minHeap.push({curr[0], {i, 0}});
        }

        Interval previousInterval = minHeap.top().first;
        while (!minHeap.empty()) {
            auto top = minHeap.top();
            minHeap.pop();

            if (previousInterval.end < top.first.start) {
                result.push_back({previousInterval.end, top.first.start});
                previousInterval = top.first;
            } else {
                previousInterval.start =
                    std::min(previousInterval.start, top.first.start);
                previousInterval.end =
                    std::max(previousInterval.end, top.first.end);
            }

            // add more of the employee's intervals if they have any
            if (top.second.second + 1 < schedule[top.second.first].size()) {
                const vector<Interval> &intervals = schedule[top.second.first];
                minHeap.push(
                    {intervals[top.second.second + 1],
                     std::pair(top.second.first, top.second.second + 1)});
            }
        }

        return result;
    }
};

int main() {
    Solution sol;

    auto result1 = sol.findEmployeeFreeTime(
        {{Interval(1, 3), Interval(5, 6)}, {Interval(2, 3), Interval(6, 8)}});
    assert(result1 == vector<Interval>{Interval(3, 5)});

    auto result2 = sol.findEmployeeFreeTime(
        {{Interval(1, 3), Interval(9, 12)}, {Interval(2, 4), Interval(6, 8)}});
    assert(result2 == vector<Interval>({Interval(4, 6), Interval(8, 9)}));

    auto result3 = sol.findEmployeeFreeTime(
        {{Interval(1, 3), Interval(2, 4)}, {Interval(3, 5), Interval(7, 9)}});
    assert(result3 == vector<Interval>{Interval(5, 7)});

    cout << "All test cases passed." << endl;

    return 0;
}
