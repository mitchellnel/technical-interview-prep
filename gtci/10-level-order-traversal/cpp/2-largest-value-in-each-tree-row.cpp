#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>

#include "tree_utils.h"

using namespace std;

class Solution {

public:
    // Method to find the largest value in each row of the binary tree
    vector<int> largestValues(TreeNode* root) {
        if (root == nullptr)
            return {};

        vector<int> result;
        
        std::queue<TreeNode*> queue;
        queue.push(root);

        while (!queue.empty()) {
            const size_t levelSize = queue.size();
            int maxRowVal = std::numeric_limits<int>::min();

            for (size_t i = 0; i < levelSize; i++) {
                TreeNode* node = queue.front();
                queue.pop();

                maxRowVal = std::max(maxRowVal, node->val);

                if (node->left != nullptr)
                    queue.push(node->left);
                
                if (node->right != nullptr)
                    queue.push(node->right);
            }

            result.push_back(maxRowVal);
        }

        return result;
    }
};

int main() {
    Solution sol = Solution();

    TreeNode* root1 = new TreeNode(4);
    root1->left = new TreeNode(5);
    root1->right = new TreeNode(10);
    root1->left->left = new TreeNode(5);
    root1->left->right = new TreeNode(7);
    std::vector<int> expected1 = {4, 10, 7};
    assert(sol.largestValues(root1) == expected1);

    TreeNode* root2 = new TreeNode(9);
    std::vector<int> expected2 = {9};
    assert(sol.largestValues(root2) == expected2);

    TreeNode* root3 = new TreeNode(1);
    root3->left = new TreeNode(2);
    root3->right = new TreeNode(3);
    root3->left->left = new TreeNode(4);
    root3->left->right = new TreeNode(5);
    root3->right->left = new TreeNode(6);
    root3->right->right = new TreeNode(7);
    std::vector<int> expected3 = {1, 3, 7};
    assert(sol.largestValues(root3) == expected3);

    std::cout << "All test cases passed." << std::endl;

    cleanupTree(root1);
    cleanupTree(root2);
    cleanupTree(root3);

    return 0;
}
