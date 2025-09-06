#include <cassert>
#include <iostream>
#include <vector>
#include <queue>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  static vector<int> traverse(TreeNode* root) {
    if (root == nullptr)
      return {};

    vector<int> rightView;

    std::queue<TreeNode*> queue;
    queue.push(root);

    while (!queue.empty()) {
      const size_t levelSize = queue.size();

      for (size_t i = 0; i < levelSize; i++) {
        TreeNode* node = queue.front();
        queue.pop();

        if (i == levelSize - 1)
          rightView.push_back(node->val);
        
        if (node->left != nullptr)
          queue.push(node->left);
        
        if (node->right != nullptr)
          queue.push(node->right);
      }
    }

    return rightView;
  }
};

int main() {
    Solution sol = Solution();
    
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->right = new TreeNode(6);
    std::vector<int> expected1 = {1, 3, 6};
    assert(sol.traverse(root) == expected1);

    TreeNode* root2 = new TreeNode(12);
    root2->left = new TreeNode(7);
    root2->right = new TreeNode(1);
    root2->left->left = new TreeNode(9);
    root2->right->left = new TreeNode(10);
    root2->right->right = new TreeNode(5);
    std::vector<int> expected2 = {12, 1, 5};
    assert(sol.traverse(root2) == expected2);

    cout << "All test cases passed." << endl;

    delete root;
    delete root2;

    return 0;
}
