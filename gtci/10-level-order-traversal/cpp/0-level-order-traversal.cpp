#include <cassert>
#include <iostream>
#include <queue>

#include "tree_utils.h"

class Solution {
    public:
    std::vector<int> getLevelOrderTraversal(TreeNode* root) {
        if (root == nullptr)
            return {};

        std::vector<int> traversal;
        
        std::queue<TreeNode*> queue;
        queue.push(root);

        while (!queue.empty()) {
            const size_t levelSize = queue.size();

            for (size_t i = 0; i < levelSize; i++) {
                TreeNode* node = queue.front();
                queue.pop();

                traversal.push_back(node->val);

                if (node->left != nullptr)
                    queue.push(node->left);
                
                if (node->right != nullptr)
                    queue.push(node->right);
            }
        }

        return traversal;
    }
};

int main() {
    Solution sol = Solution();

    // Test case 1: Tree with multiple levels
    TreeNode* root1 = new TreeNode(4);
    root1->left = new TreeNode(5);
    root1->right = new TreeNode(10);
    root1->left->left = new TreeNode(5);
    root1->left->right = new TreeNode(7);
    std::vector<int> expected1 = {4, 5, 10, 5, 7};
    assert(sol.getLevelOrderTraversal(root1) == expected1);

    // Test case 2: Single node tree
    TreeNode* root2 = new TreeNode(9);
    std::vector<int> expected2 = {9};
    assert(sol.getLevelOrderTraversal(root2) == expected2);

    std::cout << "All test cases passed." << std::endl;
    
    // Clean up memory
    cleanupTree(root1);
    cleanupTree(root2);

    return 0;
}
