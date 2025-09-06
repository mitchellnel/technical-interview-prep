#include <cassert>
#include <iostream>
#include <queue>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  vector<double> findLevelAverages(TreeNode *root) {
    if (root == nullptr)
      return {};

    vector<double> result;
    
    std::queue<TreeNode*> queue;
    queue.push(root);

    while (!queue.empty()) {
      const size_t levelSize = queue.size();

      double levelSum = 0;
      for (size_t i = 0; i < levelSize; i++) {
        TreeNode* node = queue.front();
        queue.pop();

        levelSum += node->val;

        if (node->left != nullptr)
          queue.push(node->left);

        if (node->right != nullptr)
          queue.push(node->right);
      }

      result.push_back(levelSum / static_cast<double>(levelSize));
    }

    return result;
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
    vector<double> expected1 = {1.0, 2.5, 5.5};
    assert(sol.findLevelAverages(root1) == expected1);
    
    TreeNode* root2 = new TreeNode(12);
    root2->left = new TreeNode(7);
    root2->right = new TreeNode(1);
    root2->left->left = new TreeNode(9);
    root2->left->right = new TreeNode(2);
    root2->right->right = new TreeNode(10);
    vector<double> expected2 = {12.0, 4.0, 7.0};
    assert(sol.findLevelAverages(root2) == expected2);

    TreeNode* root3 = new TreeNode(3);
    root3->left = new TreeNode(9);
    root3->right = new TreeNode(20);
    root3->right->left = new TreeNode(15);
    root3->right->right = new TreeNode(7);
    vector<double> expected3 = {3.0, 14.5, 11.0};
    assert(sol.findLevelAverages(root3) == expected3);

    std::cout << "All test cases passed." << std::endl;

    delete root1;
    delete root2;
    delete root3;

    return 0;
}
