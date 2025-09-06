#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <utility>
#include <queue>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
    // Method to find the maximum width of the binary tree
    int widthOfBinaryTree(TreeNode* root) {
        if (root == nullptr)
            return 0;
        
        int maxWidth = std::numeric_limits<int>::min();

        std::queue<std::pair<TreeNode*, int>> queue;
        queue.push({root, 0});

        while (!queue.empty()) {
            const size_t levelSize = queue.size();

            int leftmostIndex;
            int rightmostIndex;

            for (size_t i = 0; i < levelSize; i++) {
                auto [node, index] = queue.front();
                queue.pop();

                if (i == 0)
                    leftmostIndex = index;
                if (i == levelSize - 1)
                    rightmostIndex = index;
                
                if (node->left != nullptr)
                    queue.push({node->left, 2 * index});
                
                if (node->right != nullptr)
                    queue.push({node->right, 2 * index + 1});
            }

            maxWidth = std::max(maxWidth, rightmostIndex - leftmostIndex + 1);
        }
        
        return maxWidth; 
    }
};

int main() {
    Solution sol = Solution();

    TreeNode* root1 = new TreeNode(4);
    root1->left = new TreeNode(5);
    root1->right = new TreeNode(10);
    root1->left->left = new TreeNode(5);
    root1->left->right = new TreeNode(7);
    assert(sol.widthOfBinaryTree(root1) == 2);

    TreeNode* root2 = new TreeNode(9);
    assert(sol.widthOfBinaryTree(root2) == 1);

    TreeNode* root3 = new TreeNode(1);
    root3->left = new TreeNode(2);
    root3->right = new TreeNode(3);
    root3->left->left = new TreeNode(4);
    root3->left->right = new TreeNode(5);
    root3->right->left = new TreeNode(6);
    root3->right->right = new TreeNode(7);
    assert(sol.widthOfBinaryTree(root3) == 4);

    TreeNode* root4 = new TreeNode(1);
    root4->left = new TreeNode(2);
    root4->right = new TreeNode(3);
    root4->left->left = new TreeNode(4);
    root4->right->left = new TreeNode(5);
    root4->right->right = new TreeNode(6);
    root4->left->left->left = new TreeNode(7);
    assert(sol.widthOfBinaryTree(root4) == 4);

    cleanupTree(root1);
    cleanupTree(root2);
    cleanupTree(root3);
    cleanupTree(root4);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
