
def shift_string(string, shift):
    return [chr((ord(char) + shift) % 256) for char in string]

def reverse_shift_string(string, shift):
    return [chr((ord(char) - shift) % 256) for char in string]

string = "Mr. Baez"
shift = 13

encrypted_string = shift_string(string, shift)

decrypted_string = reverse_shift_string(encrypted_string, shift)

before_shift = [ord(char) for char in string]
after_shift = [ord(char) for char in encrypted_string]

print("Before shift (ASCII):" + before_shift)
print("After shift (Encrypted ASCII):" + after_shift)
print("Encrypted String:" + encrypted_string)
print("Decrypted String:" + decrypted_string)
