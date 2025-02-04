def caesar_cipher(s):
    charLst = list(chr(i) for i in range(128))
    
    
    outputstr = ''
    
    for char in s:
        indx = charLst.index(char)
        indx += 13
        if indx <= len(charLst)-1:
            outputstr += charLst[indx]
        else:
            indx = indx - len(charLst)
            outputstr += charLst[indx]
        
    return (outputstr)
    

s = input("enter string ")
print(caesar_cipher(s))
    

    
