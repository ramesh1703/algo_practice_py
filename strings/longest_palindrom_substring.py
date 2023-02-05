def longestPalindromSubstring(str):
    if len(str) < 2:
        return str
    longest = [0, 0]
    for i, _ in enumerate(str):
        j = len(str)
        while i < j:
            if longest[1] - longest[0] > j - i:
                break
            if isPalindrome(str[i:j]):
                if j - i > longest[1] - longest[0]:
                    longest = [i, j]
            j -= 1

    return str[longest[0]:longest[1]]

def isPalindrome(str):
    return str == str[::-1]

input = "abaxyzzyxf"
output = longestPalindromSubstring(input)
print(output)
