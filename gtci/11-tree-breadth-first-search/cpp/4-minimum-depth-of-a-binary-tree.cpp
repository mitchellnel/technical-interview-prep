#include <cassert>
#include <iostream>
#include <queue>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  int findDepth(TreeNode *root) {
    if (root == nullptr)
      return 0;
    
    std::queue<TreeNode*> queue;
    queue.push(root);

    int level = 1;
    while (!queue.empty()) {
      const size_t levelSize = queue.size();

      for (size_t i = 0; i < levelSize; i++) {
        TreeNode* node = queue.front();
        queue.pop();

        if (node->left == nullptr && node->right == nullptr)
          return level;
        
        if (node->left != nullptr)
          queue.push(node->left);
        
        if (node->right != nullptr)
          queue.push(node->right);
      }

      level++;
    }

    return 0;
  }
};

int main() {
    Solution sol = Solution();
    
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    assert(sol.findDepth(root) == 2);
    
    root = new TreeNode(12);
    root->left = new TreeNode(7);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(9);
    root->right->left = new TreeNode(10);
    root->right->right = new TreeNode(5);
    assert(sol.findDepth(root) == 3);
    
    root = new TreeNode(10);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->right->right = new TreeNode(15);
    root->right->right->left = new TreeNode(7);
    assert(sol.findDepth(root) == 2);

    std::cout << "All test cases passed." << std::endl;

    delete root;

    return 0;
}
