#python code that should encode "Mr. Baez" for the bellringer today w/ a shift of 13


def caesar_cipher(text, shift):
    final_text = ""
    for hrihaan in text:
        if hrihaan.isupper():
            final_text += chr(((ord(hrihaan) - 65 + shift) % 26) + 65)
        elif hrihaan.islower():
            final_text += chr(((ord(hrihaan) - 97 + shift) % 26) + 97)
        else:
            final_text += hrihaan
    return final_text

text = "Mr. Baez"
shift = 13
print(caesar_cipher(text, shift))
