#include <cassert>
#include <climits>
#include <iostream>
#include <queue>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        if (root == nullptr)
            return 0;
        
        std::queue<TreeNode*> queue;
        queue.push(root);

        int maxSum = std::numeric_limits<int>::min();
        int maxSumLevel = 0;

        int currLevel = 0;
        while (!queue.empty()) {
            const size_t levelSize = queue.size();
            currLevel++;

            int currLevelSum = 0;
            for (size_t i = 0; i < levelSize; i++) {
                TreeNode* node = queue.front();
                queue.pop();

                currLevelSum += node->val;

                if (node->left != nullptr)
                    queue.push(node->left);
                
                if (node->right != nullptr)
                    queue.push(node->right);
            }

            if (currLevelSum > maxSum) {
                maxSum = currLevelSum;
                maxSumLevel = currLevel;
            }
        }
        
        return maxSumLevel;
    }
};

int main() {
    Solution sol = Solution();

    TreeNode* root1 = new TreeNode(4);
    root1->left = new TreeNode(5);
    root1->right = new TreeNode(10);
    root1->left->left = new TreeNode(5);
    root1->left->right = new TreeNode(7);
    assert(sol.maxLevelSum(root1) == 2);

    TreeNode* root2 = new TreeNode(9);
    assert(sol.maxLevelSum(root2) == 1);

    TreeNode* root3 = new TreeNode(1);
    root3->left = new TreeNode(2);
    root3->right = new TreeNode(3);
    root3->left->left = new TreeNode(4);
    root3->left->right = new TreeNode(5);
    root3->right->left = new TreeNode(6);
    root3->right->right = new TreeNode(7);
    assert(sol.maxLevelSum(root3) == 3);

    TreeNode* root4 = new TreeNode(1);
    root4->left = new TreeNode(2);
    root4->right = new TreeNode(3);
    root4->left->left = new TreeNode(4);
    root4->right->left = new TreeNode(5);
    root4->right->right = new TreeNode(6);
    root4->left->left->left = new TreeNode(7);
    assert(sol.maxLevelSum(root4) == 3);

    cleanupTree(root1);
    cleanupTree(root2);
    cleanupTree(root3);
    cleanupTree(root4);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
