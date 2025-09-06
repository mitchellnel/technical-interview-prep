#ifndef TREE_UTILS_H
#define TREE_UTILS_H

#include <queue>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val, TreeNode* left=nullptr, TreeNode* right=nullptr) : val(val), left(left), right(right) {}
};

inline void cleanupTree(TreeNode* root) {
    std::queue<TreeNode*> queue;

    queue.push(root);

    while (!queue.empty()) {
        const size_t levelSize = queue.size();

        for (size_t i = 0; i < levelSize; i++) {
            TreeNode* node = queue.front();
            queue.pop();

            if (node->left != nullptr)
                queue.push(node->left);
            
            if (node->right != nullptr)
                queue.push(node->right);

            delete node;
        }
    }
}

#endif  // TREE_UTILS_H
