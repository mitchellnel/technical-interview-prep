# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# O(n) time | O(d) space
def productSum(array):
    return productSumHelper(array, 1)


def productSumHelper(array, depth):
    sum = 0
    for elem in array:
        if type(elem) == list:
            sum += productSumHelper(elem, depth + 1)
        else:
            sum += elem
    return depth * sum
