#ifndef TREE_UTILS_H
#define TREE_UTILS_H

#include <queue>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val, TreeNode* left=nullptr, TreeNode* right=nullptr) : val(val), left(left), right(right) {}

    ~TreeNode() {
        delete left;
        delete right;
    }
};

#endif  // TREE_UTILS_H
