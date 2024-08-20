str = input('str: ')

countu = 0
countl = 0
for char in str:
    if char.islower():
        countl += 1
    elif char.isupper():
        countu += 1

print(countl)
print(countu)
