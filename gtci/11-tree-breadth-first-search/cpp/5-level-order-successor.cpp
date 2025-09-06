#include <cassert>
#include <iostream>
#include <queue>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  TreeNode* findSuccessor(TreeNode* root, int key) {
    if (root == nullptr)
      return nullptr;

    std::queue<TreeNode*> queue;
    queue.push(root);

    bool nextNodeIsSuccessor = false;
    while (!queue.empty()) {
      TreeNode* node = queue.front();
      queue.pop();

      if (nextNodeIsSuccessor)
        return node;
      
      if (node->val == key)
        nextNodeIsSuccessor = true;
      
      if (node->left != nullptr)
        queue.push(node->left);
      
      if (node->right != nullptr)
        queue.push(node->right);
    }
    
    return nullptr;
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
    assert(sol.findSuccessor(root1, 3)->val == 4);
    assert(sol.findSuccessor(root1, 7) == nullptr);
    
    TreeNode* root2 = new TreeNode(12);
    root2->left = new TreeNode(7);
    root2->right = new TreeNode(1);
    root2->left->left = new TreeNode(9);
    root2->right->left = new TreeNode(10);
    root2->right->right = new TreeNode(5);
    assert(sol.findSuccessor(root2, 9)->val == 10);
    assert(sol.findSuccessor(root2, 12)->val == 7);
    assert(sol.findSuccessor(root2, 10)->val == 5);
    assert(sol.findSuccessor(root2, 5) == nullptr);

    std::cout << "All test cases passed." << std::endl;

    delete root1;
    delete root2;

    return 0;
}
