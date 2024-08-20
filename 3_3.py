def is_plusone_dictionary(d) :
    for i in range(len(d)) :
        if list(d.keys())[i] != list(d.values())[i] - 1 :
            return False
        if i != 0 and list(d.keys())[i] != list(d.keys())[i-1] + 2 :
             return False

    return True

print(is_plusone_dictionary({1:2, 4:5, 5:6, 7:8}))