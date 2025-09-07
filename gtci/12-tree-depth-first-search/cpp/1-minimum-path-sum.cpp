#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <limits>

#include "tree_utils.h"

class Solution {
    public:
    int getMinimumPathSum(TreeNode* root) {
        if (root == nullptr)
            return std::numeric_limits<int>::max();
        
        if (root->left == nullptr && root->right == nullptr)
            return root->val;

        return root->val + std::min(getMinimumPathSum(root->left), getMinimumPathSum(root->right));
    }
};

int main() {
    Solution sol;

    TreeNode* root = new TreeNode(10);
    root->left = new TreeNode(5);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(2);
    root->right->right = new TreeNode(1);
    assert(sol.getMinimumPathSum(root) == 16);

    delete root;

    std::cout << "All test cases passed.\n";

    return 0;
}
