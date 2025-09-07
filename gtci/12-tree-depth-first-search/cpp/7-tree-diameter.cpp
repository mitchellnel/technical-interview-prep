#include <algorithm>
#include <cassert>
#include <iostream>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  int diameter = 0;
  int findDiameter(TreeNode* root) {
    if (root == nullptr)
      return 0;
    
    longestPath(root);

    return this->diameter;
  }

  int longestPath(TreeNode* node) {
    if (node == nullptr)
      return 0;
    
    int longestLeftPath = longestPath(node->left);
    int longestRightPath = longestPath(node->right);

    this->diameter = std::max(this->diameter, longestLeftPath + longestRightPath + 1);

    return std::max(longestLeftPath, longestRightPath) + 1;
  }
};

int main() {
    Solution sol;
    
    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(3);
    root1->left->left = new TreeNode(4);
    root1->right->left = new TreeNode(5);
    root1->right->right = new TreeNode(6);
    assert(sol.findDiameter(root1) == 5);
    
    TreeNode* root2 = new TreeNode(1);
    root2->left = new TreeNode(2);
    root2->right = new TreeNode(3);
    root2->right->left = new TreeNode(5);
    root2->right->right = new TreeNode(6);
    root2->right->left->left = new TreeNode(7);
    root2->right->right->right = new TreeNode(8);
    root2->right->left->left->left = new TreeNode(9);
    root2->right->right->right->left = new TreeNode(10);
    root2->right->right->right->left->left = new TreeNode(11);
    assert(sol.findDiameter(root2) == 8);
    
    cout << "All test cases passed." << endl;

    delete root1;
    delete root2;
    
    return 0;
}
