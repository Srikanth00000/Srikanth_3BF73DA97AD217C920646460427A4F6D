def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["Apple", "Banana", "Apple", "Orange", "Apple"]
target_product = "Apple"
result = linear_search_product(products, target_product)
print(result)  # This will print [0, 2, 4], as "Apple" is found at indices 0, 2, and 4


