lower_letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

upper_letters = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}

word = list(input("Enter a message you would like to encode:"))

shift = input("Enter a number from 1 to 26:")

def cipher():
    if word in lower_letters:
        for i in range(shift):
            word = word + shift

    elif word in upper_letters:
        for i in range(shift):
            word = word + shift
    
cipher()
