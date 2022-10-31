# O(n) time | O(n) space
def arrayOfProducts(array):
    products = []

    product_of_all = None

    for num in array:
        if num == 0:
            continue
        elif product_of_all is None:
            product_of_all = num
        else:
            product_of_all *= num

    for num in array:
        if num == 0 and array.count(0) < 2:
            products.append(product_of_all)
        elif 0 in array:
            products.append(0)
        else:
            products.append(product_of_all / num)

    return products


# O(n) time | O(n) space
def arrayOfProducts_running(array):
    products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        products[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        products[i] *= right_running_product
        right_running_product *= array[i]

    return products
