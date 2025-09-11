#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>

class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x, TreeNode* left = nullptr, TreeNode* right = nullptr) : val(x), left(left), right(right) {}

    ~TreeNode() {
        delete left;
        delete right;
    }
};

class Solution {
public:
    struct pair_hash {
        template <typename T1, typename T2>
        std::size_t operator()(const std::pair<T1, T2>& p) const {
            return std::hash<T1>{}(p.first) ^ (std::hash<T2>{}(p.second) << 1);
        }
    };

    std::vector<TreeNode*> findUniqueTrees(int n) {
        if (n == 0)
            return {};

        std::unordered_map<std::pair<int, int>, std::vector<TreeNode*>, pair_hash> memo;

        return dfs(memo, 1, n);
    }

private:
    std::vector<TreeNode*> dfs(std::unordered_map<std::pair<int, int>, std::vector<TreeNode*>, pair_hash>& memo, const int& start, const int& end) {
        // base case -- no values remaining
        if (start > end)
            return { nullptr };
        
        // base case -- memoised
        if (memo.contains({start, end}))
            return memo[{start, end}];
        
        std::vector<TreeNode*> trees;
        for (int root_val = start; root_val < end + 1; root_val++) {
            std::vector<TreeNode*> leftSubtrees = dfs(memo, start, root_val - 1);
            std::vector<TreeNode*> rightSubtrees = dfs(memo, root_val + 1, end);

            for (auto left : leftSubtrees) {
                for (auto right : rightSubtrees) {
                    TreeNode* root = new TreeNode(root_val, left, right);

                    trees.push_back(root);
                }
            }
        }

        memo[{start, end}] = trees;
        return trees;
    }
};

int main() {
    Solution sol;

    // n = 0 should return 0 trees
    auto trees0 = sol.findUniqueTrees(0);
    assert(trees0.size() == 0);

    // n = 1 should return 1 tree
    auto trees1 = sol.findUniqueTrees(1);
    assert(trees1.size() == 1);

    // n = 2 should return 2 trees
    auto trees2 = sol.findUniqueTrees(2);
    assert(trees2.size() == 2);

    // n = 3 should return 5 trees
    auto trees3 = sol.findUniqueTrees(3);
    assert(trees3.size() == 5);

    std::cout << "All assertions passed." << std::endl;
    return 0;
}
