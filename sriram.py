MAX_KEY_SIZE = 26 

def rot13(message):
    key = 13 
    translated = ''

    for symbol in message:
        if symbol.isalpha():  
            num = ord(symbol)
            num += key


            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol

    return translated
    
message = "Mr. Baez"
encrypted_message = rot13(message)
print("Original Message: ", message)
print("Encrypted Message (ROT13): ", encrypted_message)
