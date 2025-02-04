def cipher(text):
    PJ = []
    
    
    for char in text: # Checks if it's uppercase/lowercase and then applies shift 13.
        
        if char.isupper():
            
            PJ.append(chr((ord(char) - 65 + 13) % 26 + 65))
       
        elif char.islower():
            
            PJ.append(chr((ord(char) - 97 + 13) % 26 + 97))
        else:
            
            PJ.append(char)
    
    
    return ''.join(PJ) # Return the final code. 


input_text = "Mr Baez"
encoded_text = cipher(input_text)
print(input_text)
print(encoded_text) 
