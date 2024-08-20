def count_minus(str):
    return sum(1 for char in str if char == '-')

print(count_minus('1 2 3 -4 -5 -6'))