#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  vector<vector<int>> traverse(TreeNode *root) {
    if (root == nullptr)
      return {};
    
    std::queue<TreeNode*> queue;
    queue.push(root);

    std::vector<std::vector<int>> traversal;
    while (!queue.empty()) {
      const size_t levelSize = queue.size();

      std::vector<int> levelTraversal;
      for (size_t i = 0; i < levelSize; i++) {
        TreeNode* node = queue.front();
        queue.pop();

        levelTraversal.push_back(node->val);

        if (node->left != nullptr)
          queue.push(node->left);
        
        if (node->right != nullptr)
          queue.push(node->right);
      }

      traversal.push_back(levelTraversal);
    }

    std::reverse(traversal.begin(), traversal.end());
    
    return traversal;
  }
};

int main() {
    Solution sol = Solution();

    TreeNode* root1 = new TreeNode(4);
    root1->left = new TreeNode(5);
    root1->right = new TreeNode(10);
    root1->left->left = new TreeNode(5);
    root1->left->right = new TreeNode(7);
    std::vector<vector<int>> expected1 = {{5, 7}, {5, 10}, {4}};
    assert(sol.traverse(root1) == expected1);

    TreeNode* root2 = new TreeNode(9);
    std::vector<vector<int>> expected2 = {{9}};
    assert(sol.traverse(root2) == expected2);

    TreeNode* root3 = new TreeNode(1);
    root3->left = new TreeNode(2);
    root3->right = new TreeNode(3);
    root3->left->left = new TreeNode(4);
    root3->left->right = new TreeNode(5);
    root3->right->left = new TreeNode(6);
    root3->right->right = new TreeNode(7);
    std::vector<vector<int>> expected3 = {{4, 5, 6, 7}, {2, 3}, {1}};
    assert(sol.traverse(root3) == expected3);

    std::cout << "All test cases passed." << std::endl;

    cleanupTree(root1);
    cleanupTree(root2);
    cleanupTree(root3);

    return 0;
}
