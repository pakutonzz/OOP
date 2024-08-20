def delete_minus(x):
    return [[num for num in unit if num >= 0] for unit in x]


print(delete_minus([[1, -3, 2], [-8, 5], [-1, -4, -3]]))