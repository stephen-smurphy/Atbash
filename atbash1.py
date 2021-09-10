
def atbash(txt):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    output = ""
    for letter in txt:
        newLetter = ""
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                newLetter = alphabet[25 - i]
            elif letter == alphabet[i].upper():
                newLetter = alphabet[25 - i].upper()
        if newLetter == "":
            output += str(letter)
        else:
            output += newLetter
    return output

    
print(atbash("test test test"))