#include <cassert>
#include <iostream>
#include <vector>

class Solution {
   public:
    std::vector<double> findAverages(const int K, const std::vector<int>& arr) {
        std::vector<double> averages;

        int window_start = 0;
        double window_sum = 0;

        for (int window_end = 0; window_end < arr.size(); window_end++) {
            window_sum += arr[window_end];

            if (window_end >= K - 1) {
                averages.push_back(window_sum / K);

                window_sum -= arr[window_start];
                window_start++;
            }
        }

        return averages;
    }
};

int main() {
    Solution sol;
    auto result =
        sol.findAverages(5, std::vector<int>{1, 3, 2, 6, -1, 4, 1, 8, 2});

    assert(result == std::vector<double>({2.2, 2.8, 2.4, 3.6, 2.8}));

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
