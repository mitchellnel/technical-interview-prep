# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# O(d) time | O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    shallower_node = None
    deeper_node = None

    descendant_one_depth = get_depth(descendantOne, topAncestor)
    descendant_two_depth = get_depth(descendantTwo, topAncestor)

    if descendant_one_depth != descendant_two_depth:
        deeper_node = (
            descendantOne
            if descendant_one_depth > descendant_two_depth
            else descendantTwo
        )
        shallower_node = (
            descendantOne
            if descendant_one_depth < descendant_two_depth
            else descendantTwo
        )

        shallower_depth = min(descendant_one_depth, descendant_two_depth)
        deeper_depth = max(descendant_one_depth, descendant_two_depth)

        while deeper_depth != shallower_depth:
            deeper_node = deeper_node.ancestor
            deeper_depth -= 1

    curr1 = shallower_node if shallower_node is not None else descendantOne
    curr2 = deeper_node if deeper_node is not None else descendantTwo

    while curr1 is not curr2:
        curr1 = curr1.ancestor
        curr2 = curr2.ancestor

    return curr1


def get_depth(descendant, top_ancestor):
    depth = 0
    curr = descendant
    while curr is not top_ancestor:
        curr = curr.ancestor
        depth += 1

    return depth
