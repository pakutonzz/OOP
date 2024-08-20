num = input()

if 0 <= int(num) <= 9 :
    n1 = int(num)
    n2 = int(num + num)
    n3 = int(num + num + num)
    n4 = int(num + num + num + num)
    print(n1 + n2 + n3 + n4)
else:
    print('Error')