def caesar_cipher(text, shift):
    result = ""
    for char in text:
        isAlpha = char.isalpha()
        if not isAlpha:
            isUpper = char.isupper()
            charCode = ord(char)
            if isUpper:
                charCode += shift
                if charCode > ord('Z'):
                    charCode -= 26
                elif charCode < ord('A'):
                    charCode += 26
            else:
                charCode += shift
                if charCode > ord('z'):
                    charCode -= 26
                elif charCode < ord('a'):
                    charCode += 26
        else:
            charCode = ord(char)
        result += chr(charCode)
    return result

text = input("Enter your message: ")
shift = 13

encrypted_text = caesar_cipher(text, shift)
print(encrypted_text)
