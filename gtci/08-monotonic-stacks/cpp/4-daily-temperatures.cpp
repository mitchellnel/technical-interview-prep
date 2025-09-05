#include <cassert>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> daysToWait(temperatures.size(), 0);
        std::stack<int> stack;

        for (int i = 0; i < temperatures.size(); i++) {
            while (!stack.empty() &&
                   temperatures[i] > temperatures[stack.top()]) {
                int stack_temp_idx = stack.top();
                stack.pop();

                daysToWait[stack_temp_idx] = i - stack_temp_idx;
            }

            stack.push(i);
        }

        return daysToWait;
    }
};

int main() {
    Solution sol;

    // Test Case 1: Normal case with various temperature changes
    {
        vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73};
        vector<int> result = sol.dailyTemperatures(temperatures);
        vector<int> expected = {1, 1, 4, 2, 1, 1, 0, 0};
        assert(result == expected &&
               "Test Case 1 Failed: Regular temperature sequence not handled "
               "correctly");
    }

    // Test Case 2: Monotonically increasing temperatures
    {
        vector<int> temperatures = {30, 40, 50, 60};
        vector<int> result = sol.dailyTemperatures(temperatures);
        vector<int> expected = {1, 1, 1, 0};
        assert(result == expected &&
               "Test Case 2 Failed: Increasing temperatures not handled "
               "correctly");
    }

    // Test Case 3: Monotonically decreasing temperatures
    {
        vector<int> temperatures = {60, 50, 40, 30};
        vector<int> result = sol.dailyTemperatures(temperatures);
        vector<int> expected = {0, 0, 0, 0};
        assert(result == expected &&
               "Test Case 3 Failed: Decreasing temperatures not handled "
               "correctly");
    }

    // Test Case 4: All same temperatures
    {
        vector<int> temperatures = {70, 70, 70, 70};
        vector<int> result = sol.dailyTemperatures(temperatures);
        vector<int> expected = {0, 0, 0, 0};
        assert(result == expected &&
               "Test Case 4 Failed: Equal temperatures not handled correctly");
    }

    // Test Case 5: Single temperature
    {
        vector<int> temperatures = {30};
        vector<int> result = sol.dailyTemperatures(temperatures);
        vector<int> expected = {0};
        assert(result == expected &&
               "Test Case 5 Failed: Single temperature not handled correctly");
    }

    // Test Case 6: Temperature spike at the end
    {
        vector<int> temperatures = {30, 30, 30, 90};
        vector<int> result = sol.dailyTemperatures(temperatures);
        vector<int> expected = {3, 2, 1, 0};
        assert(result == expected &&
               "Test Case 6 Failed: Temperature spike at end not handled "
               "correctly");
    }

    // Test Case 7: Alternating temperatures
    {
        vector<int> temperatures = {70, 60, 80, 50, 90};
        vector<int> result = sol.dailyTemperatures(temperatures);
        vector<int> expected = {2, 1, 2, 1, 0};
        assert(result == expected &&
               "Test Case 7 Failed: Alternating temperatures not handled "
               "correctly");
    }

    // Test Case 8: Repeated values with warmer day later
    {
        vector<int> temperatures = {70, 70, 70, 80};
        vector<int> result = sol.dailyTemperatures(temperatures);
        vector<int> expected = {3, 2, 1, 0};
        assert(result == expected &&
               "Test Case 8 Failed: Repeated values with warmer day not "
               "handled correctly");
    }

    cout << "All test cases passed." << endl;
    return 0;
}
