# bellRinger 2/4 p5
# create a python code that encodes the message Mr. Baez in caesar cipher with rot 13

following_message = "Mr. Baez"
value_of_shift = 13

def cipher(text, shift):
    result = ""
    for avi in text:
        if avi.isalpha():
            start = 65 if avi.isupper() else 97
            result += chr((ord(avi) - start + shift) % 26 + start)
        else:
            result += avi
    return result

encoded_message = cipher(following_message, value_of_shift)

print(f"mr baez message: {following_message}")
print(f"encoded message after caesar cipher: {encoded_message}")
