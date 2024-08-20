def char_count(str):
    ch_count = {}
    for i in range(len(str)):
        ch_count[str[i]] = str.count(str[i])

    return ch_count

print(char_count('language'))