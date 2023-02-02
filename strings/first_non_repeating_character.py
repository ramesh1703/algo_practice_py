def first_non_repeating_character(str):
    chars = {}
    for c in str:
        chars[c] = chars.get(c, 0) + 1
    for i in range(len(str)):
        char = str[i]
        if chars.get(char) == 1:
            return i
    return -1

input = "firstNonRepeatingCharacter"
print(first_non_repeating_character(input))