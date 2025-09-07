#include <algorithm>
#include <cassert>
#include <iostream>
#include <limits>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  int findMaximumPathSum(TreeNode* root) {
    if (root == nullptr)
      return 0;

    int globalMaximumSum = numeric_limits<int>::min();
    
    findMaximumPathSumHelper(root, globalMaximumSum);

    return globalMaximumSum;
  }

  int findMaximumPathSumHelper(TreeNode* node, int& globalMaximumSum) {
    if (node == nullptr)
      return 0;
    
    const int leftMaximumSum = std::max(0, findMaximumPathSumHelper(node->left, globalMaximumSum));
    const int rightMaximumSum = std::max(0, findMaximumPathSumHelper(node->right, globalMaximumSum));

    globalMaximumSum = std::max(globalMaximumSum, leftMaximumSum + rightMaximumSum + node->val);

    return std::max(leftMaximumSum, rightMaximumSum) + node->val;
  }
};

int main() {
    Solution sol;

    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(3);
    assert(sol.findMaximumPathSum(root1) == 6);

    TreeNode* root2 = new TreeNode(1);
    root2->left = new TreeNode(2);
    root2->right = new TreeNode(3);
    root2->left->left = new TreeNode(4);
    root2->right->left = new TreeNode(5);
    root2->right->right = new TreeNode(6);
    assert(sol.findMaximumPathSum(root2) == 16);

    TreeNode* root3 = new TreeNode(1);
    root3->left = new TreeNode(2);
    root3->right = new TreeNode(3);
    root3->left->left = new TreeNode(1);
    root3->left->right = new TreeNode(3);
    root3->right->left = new TreeNode(5);
    root3->right->right = new TreeNode(6);
    root3->right->left->left = new TreeNode(7);
    root3->right->left->right = new TreeNode(8);
    root3->right->right->right = new TreeNode(9);
    assert(sol.findMaximumPathSum(root3) == 31);

    TreeNode* root4 = new TreeNode(-1);
    root4->left = new TreeNode(-3);
    assert(sol.findMaximumPathSum(root4) == -1);

    TreeNode* root5 = new TreeNode(10);
    root5->left = new TreeNode(-5);
    root5->right = new TreeNode(3);
    assert(sol.findMaximumPathSum(root5) == 13);

    cout << "All test cases passed." << endl;
    
    delete root1;
    delete root2;
    delete root3;
    delete root4;
    delete root5;
    
    return 0;
}
