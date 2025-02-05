input = input("Write something: ")
key  = 13

def encrypt():
    global input
    global key
    translated = ''
    for symbol in input:
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


    print(translated)

encrypt()
