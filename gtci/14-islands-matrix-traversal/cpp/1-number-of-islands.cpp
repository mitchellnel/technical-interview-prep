#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution
{
public:
  static constexpr int WATER_DEF = 0;
  static constexpr int LAND_DEF = 1;

  int countIslands(vector<vector<int>> &matrix)
  {
    const int N_ROWS = matrix.size();
    const int N_COLS = matrix[0].size();

    int totalIslands = 0;
    for (int i = 0; i < N_ROWS; i++) {
      for (int j = 0; j < N_COLS; j++) {
        if (matrix[i][j] == LAND_DEF) {
          totalIslands++;
          exploreIsland(i, j, matrix);
        }
      }
    }

    return totalIslands;
  }

private:
  void exploreIsland(const int startRow, const int startCol, vector<vector<int>>& matrix) {
    std::queue<std::pair<int, int>> queue;
    queue.push({startRow, startCol});

    while (!queue.empty()) {
      const auto [row, col] = queue.front();
      queue.pop();

      matrix[row][col] = WATER_DEF;

      const std::vector<std::pair<int, int>> directions {
        {-1, 0}, {1, 0}, {0, -1}, {0, 1}
      };
      
      for (const auto& [dr, dc] : directions) {
        const int nr = row + dr;
        const int nc= col + dc;

        if (nr >= 0 && nr < matrix.size() && nc >= 0 && nc < matrix[0].size() && matrix[nr][nc] == LAND_DEF)
          queue.push({nr, nc});
      }
    }
  }
};

int main() {
    Solution sol;

     vector<vector<int>> vec = vector<vector<int>>{
        {1, 1, 1, 0, 0},
        {0, 1, 0, 0, 1},
        {0, 0, 1, 1, 0},
        {0, 0, 1, 0, 0},
        {0, 0, 1, 0, 0}};
    assert(sol.countIslands(vec) == 3);

    vec = {
        {0, 1, 1, 1, 0},
        {0, 0, 0, 1, 1},
        {0, 1, 1, 1, 0},
        {0, 1, 1, 0, 0},
        {0, 0, 0, 0, 0}};
    assert(sol.countIslands(vec) == 1);

    cout << "All test cases passed." << endl;

    return 0;
}
