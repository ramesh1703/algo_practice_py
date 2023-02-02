def palindrome(pal):
    if len(pal) <= 1:
        return pal
    i, j = 0, len(pal) - 1
    while i < j:
        if pal[i] != pal[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

def quick_palindrome(pal):
    return pal == pal[::-1]

input = "ABBA"
output = quick_palindrome(input)
print(output)
