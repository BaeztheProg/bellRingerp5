def Message():
    print('What do you want to encrypt?')
    return input()

def rot13(message):
    encrpyt = ''
    for symbol in message:
        if symbol.isalpha():
            shift = 13
            if symbol.islower():
                num = ord(symbol) + shift
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            else:
                num = ord(symbol) + shift
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            encrpyt += chr(num)
        else:
            encrpyt += ord(symbol)

    return encrpyt

message = Message()
print('Here is the encrypted message: ')
print(rot13(message))
