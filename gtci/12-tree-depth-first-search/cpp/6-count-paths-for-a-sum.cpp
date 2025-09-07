#include <cassert>
#include <iostream>
#include <vector>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  int countPaths(TreeNode* root, int S) {
    if (root == nullptr)
      return 0;

    return countPathsHelper(root, S)
      + countPaths(root->left, S)
      + countPaths(root->right, S);
  }

  int countPathsHelper(TreeNode* node, int S) {
    if (node == nullptr)
      return 0;
    
    int count = 0;
    if (node->val == S)
      count = 1;
    
    count += countPathsHelper(node->left, S - node->val);
    count += countPathsHelper(node->right, S - node->val);

    return count;
  }
};

int main() {
    Solution sol;

    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(7);
    root1->right = new TreeNode(9);
    root1->left->left = new TreeNode(6);
    root1->left->right = new TreeNode(5);
    root1->right->left = new TreeNode(2);
    root1->right->right = new TreeNode(3);
    assert(sol.countPaths(root1, 12) == 3);

    
    TreeNode* root2 = new TreeNode(12);
    root2->left = new TreeNode(7);
    root2->right = new TreeNode(1);
    root2->left->left = new TreeNode(4);
    root2->right->left = new TreeNode(10);
    root2->right->right = new TreeNode(5);
    assert(sol.countPaths(root2, 11) == 2);

    TreeNode* root3 = new TreeNode(4);
    root3->left = new TreeNode(4);
    root3->right = new TreeNode(4);
    root3->left->left = new TreeNode(4);
    root3->left->right = new TreeNode(4);
    root3->right->left = new TreeNode(4);
    root3->right->right = new TreeNode(4);
    root3->left->left->left = new TreeNode(4);
    root3->left->left->right = new TreeNode(4);
    root3->left->right->left = new TreeNode(4);
    root3->left->right->right = new TreeNode(4);
    assert(sol.countPaths(root3, 8) == 10);

    std::cout << "All test cases passed.\n";
    
    return 0;
}
