#include <cassert>
#include <iostream>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  int findSumOfPathNumbers(TreeNode *root) {
    if (root == nullptr)
      return 0;
  
    return findSumOfPathNumbersHelper(root, 0);
  }

  int findSumOfPathNumbersHelper(TreeNode* node, int currentNumber) {
    if (node == nullptr)
      return 0;
    
    currentNumber = currentNumber * 10 + node->val;

    if (node->left == nullptr && node->right == nullptr)
      return currentNumber;
    
    return findSumOfPathNumbersHelper(node->left, currentNumber) + findSumOfPathNumbersHelper(node->right, currentNumber);
  }
};

int main() {
    Solution sol;

    TreeNode *root1 = new TreeNode(1);
    root1->left = new TreeNode(7);
    root1->right = new TreeNode(9);
    root1->right->left = new TreeNode(2);
    root1->right->right = new TreeNode(9);
    assert(sol.findSumOfPathNumbers(root1) == 408);
    
    TreeNode *root2 = new TreeNode(1);
    root2->left = new TreeNode(0);
    root2->right = new TreeNode(1);
    root2->left->left = new TreeNode(1);
    root2->right->left = new TreeNode(6);
    root2->right->right = new TreeNode(5);
    assert(sol.findSumOfPathNumbers(root2) == 332);
    
    cout << "All test cases passed." << endl;

    delete root1;
    delete root2;

    return 0;
}
