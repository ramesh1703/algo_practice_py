def generateDocument(characters, document):
    for c in characters:
        c_count = charFrequency(characters, c)
        d_count = charFrequency(document, c)
        if (d_count > c_count):
            return False
    return True

def charFrequency(str, target):
    freq = 0
    for c in str:
        if c == target:
            freq += 1
    return freq

c_input = "Bste!hetsi ogEAxpelrt x "
d_input = "AlgoExpert is the Best!"

output = generateDocument(c_input, d_input)
print(output)
