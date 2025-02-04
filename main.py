import string
message = input("Message to encrypt: ")
shift = int(input('What is the shift?'))

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
special = list(string.punctuation)

encrypted_message = ""

for letter in message:
    for i, e in enumerate(lower):
        if e == letter:
            encrypted_message += lower[(i+shift)%len(lower)]
    for i, e in enumerate(upper):
        if e == letter:
            encrypted_message += upper[(i+shift)%len(upper)]
    for i, e in enumerate(special):
        if e == letter:
            encrypted_message += special[(i+shift)%len(special)]

print(encrypted_message)
