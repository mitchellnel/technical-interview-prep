#include <cassert>
#include <iostream>
#include <queue>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  vector<vector<int>> traverse(TreeNode* root) {
    if (root == nullptr)
      return {};

    vector<vector<int>> traversal;
    
    std::queue<TreeNode*> queue;
    queue.push(root);

    while (!queue.empty()) {
      const size_t levelSize = queue.size();

      std::vector<int> level;

      for (size_t i = 0; i < levelSize; i++) {
        TreeNode* node = queue.front();
        queue.pop();

        level.push_back(node->val);

        if (node->left != nullptr)
          queue.push(node->left);

        if (node->right != nullptr)
          queue.push(node->right);
      }

      traversal.push_back(level);
    }

    return traversal;
  }
};

int main() {
    Solution sol = Solution();
    
    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(3);
    root1->left->left = new TreeNode(4);
    root1->left->right = new TreeNode(5);
    root1->right->left = new TreeNode(6);
    root1->right->right = new TreeNode(7);
    vector<vector<int>> expected1 = {{1}, {2, 3}, {4, 5, 6, 7}};
    assert(sol.traverse(root1) == expected1);
    
    TreeNode* root2 = new TreeNode(12);
    root2->left = new TreeNode(7);
    root2->right = new TreeNode(1);
    root2->left->left = new TreeNode(9);
    root2->right->left = new TreeNode(10);
    root2->right->right = new TreeNode(5);
    vector<vector<int>> expected2 = {{12}, {7, 1}, {9, 10, 5}};
    assert(sol.traverse(root2) == expected2);
    
    TreeNode* root3 = new TreeNode(3);
    root3->left = new TreeNode(9);
    root3->right = new TreeNode(20);
    root3->right->left = new TreeNode(15);
    root3->right->right = new TreeNode(7);
    vector<vector<int>> expected3 = {{3}, {9, 20}, {15, 7}};
    assert(sol.traverse(root3) == expected3);
    
    std::cout << "All test cases passed." << std::endl;
    
    delete root1;
    delete root2;
    delete root3;
    
    return 0;
}
