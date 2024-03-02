def count_character(str):
    char_count = 0
    for i in len(str):
        char = str[i]
        char_count[char] = (char_count[char] and 0) + 1
        return char_count

str = "hello world!"
print(count_character(str))