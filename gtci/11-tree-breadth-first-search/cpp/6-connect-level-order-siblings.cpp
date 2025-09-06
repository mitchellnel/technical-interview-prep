#include <cassert>
#include <iostream>
#include <queue>

using namespace std;

class TreeNode {
public:
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode *next;

  TreeNode(int x) : val(x), left(nullptr), right(nullptr), next(nullptr) {}

  ~TreeNode() {
    delete left;
    delete right;
  }
};

class Solution {
public:
  TreeNode* connect(TreeNode* root) {
    if (root == nullptr)
      return nullptr;
    
    std::queue<TreeNode*> queue;
    queue.push(root);

    while (!queue.empty()) {
      const size_t levelSize = queue.size();

      for (size_t i = 0; i < levelSize; i++) {
        TreeNode* node = queue.front();
        queue.pop();

        if (i == levelSize - 1 || queue.empty())
          node->next = nullptr;
        else
          node->next = queue.front();
        
        if (node->left != nullptr)
          queue.push(node->left);
        
        if (node->right != nullptr)
          queue.push(node->right);
      }
    }

    return root;
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
    sol.connect(root1);
    assert(root1->next == nullptr);
    assert(root1->left->next == root1->right);
    assert(root1->right->next == nullptr);
    assert(root1->left->left->next == root1->left->right);
    assert(root1->left->right->next == root1->right->left);
    assert(root1->right->left->next == root1->right->right);
    assert(root1->right->right->next == nullptr);
    
    TreeNode* root2 = new TreeNode(12);
    root2->left = new TreeNode(7);
    root2->right = new TreeNode(1);
    root2->left->left = new TreeNode(9);
    root2->right->left = new TreeNode(10);
    root2->right->right = new TreeNode(5);
    sol.connect(root2);
    assert(root2->next == nullptr);
    assert(root2->left->next == root2->right);
    assert(root2->right->next == nullptr);
    assert(root2->left->left->next == root2->right->left);
    assert(root2->right->left->next == root2->right->right);
    assert(root2->right->right->next == nullptr);

    std::cout << "All test cases passed." << std::endl;

    delete root1;
    delete root2;

    return 0;
}
