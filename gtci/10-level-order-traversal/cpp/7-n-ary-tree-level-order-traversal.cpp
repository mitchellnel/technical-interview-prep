#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class NAryNode {
public:
    int val; 
    vector<NAryNode*> children; 

    NAryNode() {
        children = vector<NAryNode*>(); 
    }

    NAryNode(int _val) {
        val = _val;
        children = vector<NAryNode*>(); 
    }

    NAryNode(int _val, vector<NAryNode*> _children) {
        val = _val;
        children = _children; 
    }

    ~NAryNode() {
        for (auto child : this->children)
            delete child;
    }
};

class Solution {
public:
    vector<vector<int>> levelOrder(NAryNode* root) {
        if (root == nullptr)
            return {};

        vector<vector<int>> traversal;

        std::queue<NAryNode*> queue;
        queue.push(root);

        while (!queue.empty()) {
            const size_t levelSize = queue.size();

            std::vector<int> level;
            for (size_t i = 0; i < levelSize; i++) {
                NAryNode* node = queue.front();
                queue.pop();

                level.push_back(node->val);

                for (NAryNode* child : node->children)
                    queue.push(child);
            }

            traversal.push_back(level);
        }
        
        return traversal;
    }
};

int main() {
    Solution sol = Solution();

    NAryNode* root1 = new NAryNode(1);
    root1->children = {new NAryNode(3), new NAryNode(2), new NAryNode(4)};
    root1->children[0]->children = {new NAryNode(5), new NAryNode(6)};
    std::vector<vector<int>> expected1 = {{1}, {3, 2, 4}, {5, 6}};
    assert(sol.levelOrder(root1) == expected1);

    NAryNode* root2 = new NAryNode(1);
    std::vector<vector<int>> expected2 = {{1}};
    assert(sol.levelOrder(root2) == expected2);

    NAryNode* root3 = nullptr;
    std::vector<vector<int>> expected3;
    assert(sol.levelOrder(root3) == expected3);

    NAryNode* root4 = new NAryNode(10);
    root4->children = {new NAryNode(15), new NAryNode(12)};
    root4->children[0]->children = {new NAryNode(20)};
    root4->children[1]->children = {new NAryNode(25)};
    root4->children[0]->children[0]->children = {new NAryNode(30), new NAryNode(40)};
    std::vector<vector<int>> expected4 = {{10}, {15, 12}, {20, 25}, {30, 40}};
    assert(sol.levelOrder(root4) == expected4);

    std::cout << "All test cases passed." << std::endl;

    delete root1;
    delete root2;
    delete root3;
    delete root4;

    return 0;
}
