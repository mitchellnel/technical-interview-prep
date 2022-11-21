# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    nodes = []

    parents = {}
    dfs_parent(tree, None, parents)

    # get the target node
    target_node = None
    for key in parents:
        if key.value == target:
            target_node = key
            break

    # graph-like bfs from target node
    queue = [(target_node, 0)]
    visited = []
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node[0])

        left = current_node[0].left
        right = current_node[0].right
        parent = parents[current_node[0]]

        dist = current_node[1]

        if dist == k:
            nodes.append(current_node[0].value)
            continue

        if left is not None and left not in visited:
            queue.append((left, dist + 1))
        if right is not None and right not in visited:
            queue.append((right, dist + 1))
        if parent is not None and parent not in visited:
            queue.append((parent, dist + 1))

    return nodes


def dfs_parent(tree, parent, parents):
    if tree is not None:
        parents[tree] = parent

        dfs_parent(tree.left, tree, parents)
        dfs_parent(tree.right, tree, parents)

    return parents
