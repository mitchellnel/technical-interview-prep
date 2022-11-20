# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(h) time | O(1) space
def validateThreeNodes_h(nodeOne, nodeTwo, nodeThree):
    # we can use the same is_ancestor function to check for being a descendant
    # if nodeThree is a descendant of nodeTwo, then nodeTwo is an ancestor of nodeThree
    if is_ancestor(nodeOne, nodeTwo) and is_ancestor(nodeTwo, nodeThree):
        return True
    elif is_ancestor(nodeThree, nodeTwo) and is_ancestor(nodeTwo, nodeOne):
        return True
    else:
        return False


def is_ancestor(node_one, node_two):
    """Returns Boolean based on whether nodeTwo is an ancestor of nodeOne"""
    # work down from node two
    current_node = node_two
    while current_node is not None:
        if current_node == node_one:
            return True

        if node_one.value < current_node.value:
            current_node = current_node.left
        else:
            current_node = current_node.right

    return False


# O(d) time | O(1) space
def validateThreeNodes(node_one, node_two, node_three):
    # we will try and find nodeTwo from nodeOne and nodeThree
    search_one = node_one
    search_two = node_three

    while True:
        # return False if we've reached node_three from node_one or
        #     node_one from node_three, in which case we didn't
        #     find node_two
        if search_one is node_three or search_two is node_one:
            return False
        # break if we find node two - we now need to check that we can
        #    reach node_one or node_three from our found node_two
        if search_one is node_two or search_two is node_two:
            break
        # return False if we finished searching without finding node_two
        if search_one is None and search_two is None:
            return False

        if search_one is not None:
            if node_two.value < search_one.value:
                search_one = search_one.left
            else:
                search_one = search_one.right

        if search_two is not None:
            if node_two.value < search_two.value:
                search_two = search_two.left
            else:
                search_two = search_two.right

    if search_one is node_two:
        return findTargetFromNode(node_three, node_two)
    else:
        return findTargetFromNode(node_one, node_two)


def findTargetFromNode(target, node):
    while node is not None:
        if node is target:
            return True

        if target.value < node.value:
            node = node.left
        else:
            node = node.right
    return False
