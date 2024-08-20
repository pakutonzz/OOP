def only_english(string1):
    str = [str for str in string1 if str.isalpha()]
    return ''.join(str)

print(only_english('12345678'))