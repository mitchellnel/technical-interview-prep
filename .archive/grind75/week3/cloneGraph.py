# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if node is None:
            return node

        queue = [node]
        clones = {node.val: Node(node.val, [])}
        while len(queue) > 0:
            curr_node = queue.pop(0)
            curr_clone = clones[curr_node.val]

            for neighbour in curr_node.neighbors:
                if neighbour.val not in clones:
                    clones[neighbour.val] = Node(neighbour.val, [])
                    queue.append(neighbour)

                curr_clone.neighbors.append(clones[neighbour.val])

        return clones[node.val]
