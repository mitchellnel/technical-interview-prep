#include <cassert>
#include <iostream>

#include "tree_utils.h"

class Solution {
public:
  static bool hasPath(TreeNode* root, int sum) {
    if (root == nullptr)
      return false;
    
    if (root->left == nullptr && root->right == nullptr)
      return root->val == sum;
    
    return hasPath(root->left, sum - root->val) || hasPath(root->right, sum - root->val);
  }
};

int main() {
    TreeNode* root = new TreeNode(12);
    root->left = new TreeNode(7);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(9);
    root->right->left = new TreeNode(10);
    root->right->right = new TreeNode(5);
    assert(Solution::hasPath(root, 23));
    assert(!Solution::hasPath(root, 16));
    
    delete root;

    std::cout << "All test cases passed.\n";

    return 0;
}
