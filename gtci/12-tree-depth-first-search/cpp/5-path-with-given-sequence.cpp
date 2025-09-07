#include <cassert>
#include <iostream>
#include <vector>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
  bool findPath(TreeNode* root, const vector<int>& sequence) {
    if (root == nullptr && sequence.empty())
      return true;

    std::vector<int> currPath;
    
    return findPathHelper(root, sequence, currPath);
  }

  bool findPathHelper(TreeNode* node, const vector<int>& sequence, vector<int>& currPath) {
    if (node == nullptr)
      return false;
    
    currPath.push_back(node->val);

    if (node->left == nullptr && node->right == nullptr && sequence == currPath) {
      currPath.pop_back();
      return true;
    }
    
    if (findPathHelper(node->left, sequence, currPath) || findPathHelper(node->right, sequence, currPath)) {
      currPath.pop_back();
      return true;
    }

    currPath.pop_back();
    return false;
  }
};

int main() {
    Solution sol;
    
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(0);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(1);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(5);
    
    vector<int> sequence = {1, 0, 7};
    assert(!sol.findPath(root, sequence));
    
    sequence = {1, 1, 6};
    assert(sol.findPath(root, sequence));
    
    sequence = {1, 0, 1};
    assert(sol.findPath(root, sequence));
    
    sequence = {1, 1, 1};
    assert(!sol.findPath(root, sequence));

    std::cout << "All test cases passed." << std::endl;

    delete root;
    
    return 0;
}
