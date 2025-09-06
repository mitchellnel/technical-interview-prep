#include <cassert>
#include <deque>
#include <iostream>
#include <queue>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  vector<vector<int>> traverse(TreeNode *root) {
    if (root == nullptr)
      return {};

    vector<vector<int>> traversal;
    
    std::queue<TreeNode*> queue;
    queue.push(root);

    bool zigzag = false;

    while (!queue.empty()) {
      const size_t levelSize = queue.size();

      std::deque<int> level;
      for (size_t i = 0; i < levelSize; i++) {
        TreeNode* node = queue.front();
        queue.pop();

        if (zigzag)
          level.push_front(node->val);
        else
          level.push_back(node->val);
        
        if (node->left != nullptr)
          queue.push(node->left);
        
        if (node->right != nullptr)
          queue.push(node->right);
      }

      traversal.push_back(std::vector<int>(level.begin(), level.end()));
      zigzag = !zigzag;
    }
    
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
    std::vector<vector<int>> expected1 = {{4}, {10, 5}, {5, 7}};
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
    std::vector<vector<int>> expected3 = {{1}, {3, 2}, {4, 5, 6, 7}};
    assert(sol.traverse(root3) == expected3);

    TreeNode* root4 = new TreeNode(1);
    root4->left = new TreeNode(2);
    root4->right = new TreeNode(3);
    root4->left->left = new TreeNode(4);
    root4->right->left = new TreeNode(5);
    root4->right->right = new TreeNode(6);
    root4->left->left->left = new TreeNode(7);
    std::vector<vector<int>> expected4 = {{1}, {3, 2}, {4, 5, 6}, {7}};
    assert(sol.traverse(root4) == expected4);

    cleanupTree(root1);
    cleanupTree(root2);
    cleanupTree(root3);
    cleanupTree(root4);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
