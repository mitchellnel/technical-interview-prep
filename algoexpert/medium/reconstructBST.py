# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n^2) time | O(n) space
def reconstructBst_n2(preOrderTraversalValues):
    print(preOrderTraversalValues)
    if not preOrderTraversalValues:
        return None
    elif len(preOrderTraversalValues) == 1:
        return BST(preOrderTraversalValues[0])

    root = BST(preOrderTraversalValues[0])

    first_gte_idx = len(preOrderTraversalValues)
    for idx, val in enumerate(preOrderTraversalValues[1:]):
        if val >= root.value:
            first_gte_idx = idx + 1
            break

    root.left = reconstructBst_n2(preOrderTraversalValues[1:first_gte_idx])
    root.right = reconstructBst_n2(preOrderTraversalValues[first_gte_idx:])

    return root


class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx


# O(n) time | O(n) space
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBSTHelper(
        float("-inf"), float("inf"), preOrderTraversalValues, treeInfo
    )


def reconstructBSTHelper(
    lowerBound, upperBound, preOrderTraversalValues, currSubtreeInfo
):
    if currSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None

    rootVal = preOrderTraversalValues[currSubtreeInfo.rootIdx]
    if rootVal < lowerBound or rootVal >= upperBound:
        return None

    currSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBSTHelper(
        lowerBound, rootVal, preOrderTraversalValues, currSubtreeInfo
    )
    rightSubtree = reconstructBSTHelper(
        rootVal, upperBound, preOrderTraversalValues, currSubtreeInfo
    )

    return BST(rootVal, leftSubtree, rightSubtree)
