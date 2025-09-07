#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

#include "tree_utils.h"

class Solution {
public:
  vector<vector<int>> findPaths(TreeNode* root, int sum) {
    vector<vector<int>> allPaths;
    vector<int> path;
    
    findPathsHelper(root, sum, allPaths, path);

    return allPaths;
  }

  void findPathsHelper(TreeNode* root, int sum, std::vector<std::vector<int>>& results, std::vector<int>& path) {
    if (root == nullptr)
      return;

    path.push_back(root->val);
    
    if (root->left == nullptr && root->right == nullptr && root->val == sum) {
      results.push_back(path);
    } else {
      findPathsHelper(root->left, sum - root->val, results, path);
      findPathsHelper(root->right, sum - root->val, results, path);
    }

    path.pop_back();
  }
};

int main() {
    Solution sol;
    TreeNode* root = new TreeNode(12);
    root->left = new TreeNode(7);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(9);
    root->left->right = new TreeNode(-3);
    root->right->left = new TreeNode(10);
    root->right->right = new TreeNode(3);

    assert(sol.findPaths(root, 23) == vector<vector<int>>({{12, 1, 10}}));
    assert(sol.findPaths(root, 16) == vector<vector<int>>({{12, 7, -3}, {12, 1, 3}}));

    delete root;

    std::cout << "All test cases passed.\n";

    return 0;
}
