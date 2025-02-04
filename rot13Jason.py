letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j" ,"k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Cletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
message = "Mr. Baez"
encoded_message= ""
for character in message:
    if character in letters:
        encoded_message += letters[(letters.index(character) + 13) % 26]
    elif character in Cletters:
        encoded_message += Cletters[(Cletters.index(character) + 13) % 26]
print(encoded_message)
