small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

msg = input("message: ")
shift_num = int(input("shift: "))

encrypted_msg = ""

for letter in msg:
    if letter in caps:
        encrypted_msg += caps[(caps.index(letter) + shift_num) % len(caps)]
    elif letter in small:
        encrypted_msg += small[(small.index(letter) + shift_num) % len(small)]
    elif letter in special_chars:
        encrypted_msg += special_chars[(special_chars.index(letter) + shift_num) % len(special_chars)]
    else:
        encrypted_msg += letter

print("encrypted message:", encrypted_msg)
