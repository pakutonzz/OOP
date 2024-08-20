def add2list(lst1, lst2) :
    for i in range(len(lst1)) :
        lst1[i] += lst2[i]
    return lst1

print(add2list([1, 2, 3], [4, 5, 6]))