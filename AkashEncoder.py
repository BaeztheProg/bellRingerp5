def caesar_cipher(text):
    result = ''
    for char in text:
        if char.isupper():
            result += chr(((ord(char) - ord('A') + 1) % 26) + ord('A'))
        elif char.islower():
            result += chr(((ord(char) - ord('a') + 1) % 26) + ord('a'))
        elif char == '.':
            result += '/'
        else:
            result += char
    return result
print(caesar_cipher("Mr. Baez"))
