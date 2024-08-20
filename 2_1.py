
numbers = input().split()

numbers.sort()

if numbers[0] == '0' :
    numbers[0], numbers[1] = numbers[1], numbers[0]


print(''.join(numbers))