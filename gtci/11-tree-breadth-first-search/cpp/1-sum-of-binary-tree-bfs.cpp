#include <cassert>
#include <iostream>
#include <queue>

#include "tree_utils.h"

class Solution {
    public:
    int sumOfBinaryTree(TreeNode* root) {
        if (root == nullptr)
            return 0;

        int sum = 0;

        std::queue<TreeNode*> queue;
        queue.push(root);

        while (!queue.empty()) {
            TreeNode* node = queue.front();
            queue.pop();

            sum += node->val;

            if (node->left != nullptr)
                queue.push(node->left);
            
            if (node->right != nullptr)
                queue.push(node->right);
        }

        return sum;
    }
};

int main() {
    Solution sol = Solution();

    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(3);
    assert(sol.sumOfBinaryTree(root1) == 6);
    
    TreeNode* root2 = new TreeNode(4);
    root2->left = new TreeNode(9);
    root2->right = new TreeNode(7);
    root2->left->left = new TreeNode(2);
    root2->left->right = new TreeNode(6);
    assert(sol.sumOfBinaryTree(root2) == 28);

    TreeNode* root3 = new TreeNode(10);
    root3->left = new TreeNode(5);
    root3->right = new TreeNode(3);
    root3->left->left = new TreeNode(7);
    root3->right->right = new TreeNode(9);
    assert(sol.sumOfBinaryTree(root3) == 34);

    std::cout << "All test cases passed." << std::endl;

    delete root1;
    delete root2;
    delete root3;

    return 0;
}
