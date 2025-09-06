#include <cassert>
#include <climits>
#include <iostream>
#include <queue>

#include "tree_utils.h"

using namespace std;

class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        if (root == nullptr)
            return true;
        
        std::queue<TreeNode*> queue;
        queue.push(root);

        int level = -1;
        while (!queue.empty()) {
            const size_t levelSize = queue.size();
            level++;

            int prevNodeValue;
            if (level % 2 == 0)
                prevNodeValue = std::numeric_limits<int>::min();
            else
                prevNodeValue = std::numeric_limits<int>::max();

            for (size_t i = 0; i < levelSize; i++) {
                TreeNode* node = queue.front();
                queue.pop();

                if (level % 2 == 0) {
                    if (node->val % 2 == 0 || node->val <= prevNodeValue)
                        return false;
                } else {
                    if (node->val % 2 != 0 || node->val >= prevNodeValue)
                        return false;
                }

                if (node->left != nullptr)
                    queue.push(node->left);
                
                if (node->right != nullptr)
                    queue.push(node->right);
                
                prevNodeValue = node->val;
            }
        }

        return true;
    }
};

int main() {
    Solution sol = Solution();

    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(10);
    root1->right = new TreeNode(4);
    root1->left->left = new TreeNode(3);
    root1->left->right = new TreeNode(7);
    assert(sol.isEvenOddTree(root1));

    TreeNode* root2 = new TreeNode(5);
    root2->left = new TreeNode(9);
    root2->right = new TreeNode(3);
    root2->left->left = new TreeNode(12);
    root2->right->right = new TreeNode(8);
    assert(!sol.isEvenOddTree(root2));

    TreeNode* root3 = new TreeNode(7);
    root3->left = new TreeNode(10);
    root3->right = new TreeNode(2);
    root3->left->left = new TreeNode(12);
    root3->left->right = new TreeNode(8);
    assert(!sol.isEvenOddTree(root3));

    std::cout << "All test cases passed." << std::endl;

    cleanupTree(root1);
    cleanupTree(root2);
    cleanupTree(root3);

    return 0;
}
