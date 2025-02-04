input_text = "Mr.Baez"
shift = 13

def caesar_cipher(text, shift):
    result = ""
    
    for hanu in text:
        if hanu.isupper():
            
            x = ord('A') if hanu.islower() else ord('a')
            
            result += chr((ord(hanu) - x + shift) % 26 + x)
        else:
            
            result += hanu
    
    return result

encoded_text = caesar_cipher(input_text, shift)
print(f"text: {encoded_text}")
