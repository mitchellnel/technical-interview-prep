#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
   public:
    std::priority_queue<int> maxHeap;
    int findMaximumCapital(
      const vector<int>& capital,
      const vector<int>& profits,
      int numberOfProjects,
      int initialCapital
    ) {
      std::vector<std::pair<int, int>> projects;
      for (size_t i = 0; i < capital.size(); i++)
        projects.push_back({capital[i], profits[i]});
      
      std::sort(projects.begin(), projects.end(), [](auto& a, auto& b) { return a.first < b.first; });

      int capitalAvailable = initialCapital;
      int nextProjectToConsider = 0;
      
      for (int i = 0; i < numberOfProjects; i++) {
        nextProjectToConsider = populateMaxHeap(nextProjectToConsider, projects, capitalAvailable);

        if (maxHeap.empty())
          break;
        
        int profit = maxHeap.top();
        maxHeap.pop();

        capitalAvailable += profit;
      }

      return capitalAvailable;
    }

    int populateMaxHeap(
      const int& nextProjectToConsider,
      const std::vector<std::pair<int, int>>& projects,
      const int& availableCapital
    ) {
      int project = nextProjectToConsider;
      while (project < projects.size() && projects[project].first <= availableCapital) {
        maxHeap.push(projects[project].second);
        project++;
      }

      return project;
    }
};

int main() {
    Solution solution;

    assert(solution.findMaximumCapital({0, 1, 2}, {1, 2, 3}, 2, 1) == 6);
    assert(solution.findMaximumCapital({0, 1, 2, 3}, {1, 2, 3, 5}, 3, 0) == 8);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
