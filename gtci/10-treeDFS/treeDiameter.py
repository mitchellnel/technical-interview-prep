class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class TreeDiameter:
    def __init__(self):
        self.tree_diameter = 0

    def find_tree_diameter(self, root):
        self._get_tree_height(root)
        return self.tree_diameter

    def _get_tree_height(self, tree):
        # DFS
        # base case
        if tree is None:
            return 0

        # recursive step
        left_tree_height = self._get_tree_height(tree.left)
        right_tree_height = self._get_tree_height(tree.right)

        # if the current node does not have a left or right subtree, no path passes through it
        if left_tree_height != 0 and right_tree_height != 0:
            # calculate diameter at current node
            diameter = left_tree_height + right_tree_height + 1

            # get max diameter
            self.tree_diameter = max(self.tree_diameter, diameter)

        # return the max height of the subtrees of this node, plus 1 for current node
        return max(left_tree_height, right_tree_height) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_tree_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    root.right.right.left.left.left = TreeNode(12)
    print("Tree Diameter: " + str(treeDiameter.find_tree_diameter(root)))


main()
