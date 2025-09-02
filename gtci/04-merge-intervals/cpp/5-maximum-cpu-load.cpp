#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Job {
   public:
    int start = 0;
    int end = 0;
    int cpuLoad = 0;

    Job(int start, int end, int cpuLoad) {
        this->start = start;
        this->end = end;
        this->cpuLoad = cpuLoad;
    }
};

class Solution {
   public:
    int findMaxCPULoad(vector<Job>&& jobs) {
        if (jobs.size() == 0) return 0;

        if (jobs.size() == 1) return jobs[0].cpuLoad;

        std::sort(jobs.begin(), jobs.end(),
                  [](Job a, Job b) { return a.start < b.start; });

        auto jobCmp = [](const Job& a, const Job& b) { return a.end > b.end; };
        std::priority_queue<Job, std::vector<Job>, decltype(jobCmp)> minHeap(
            jobCmp);

        int maxCpuLoad = 0;
        int currentCpuLoad = 0;

        for (Job& job : jobs) {
            while (!minHeap.empty() && minHeap.top().end <= job.start) {
                const Job& poppedJob = minHeap.top();
                minHeap.pop();
                currentCpuLoad -= poppedJob.cpuLoad;
            }

            minHeap.push(job);
            currentCpuLoad += job.cpuLoad;

            maxCpuLoad = std::max(maxCpuLoad, currentCpuLoad);
        }

        return maxCpuLoad;
    }
};

int main() {
    Solution sol;

    assert(sol.findMaxCPULoad({Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)}) == 7);
    assert(sol.findMaxCPULoad({Job(6, 7, 2), Job(2, 4, 11), Job(8, 12, 15)}) ==
           15);
    assert(sol.findMaxCPULoad({Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)}) == 8);

    cout << "All test cases passed." << endl;

    return 0;
}
