def encrypt(text, shift):
  result = ''
  for letter in text:
    if letter.isalpha():
      start = ord('a') if letter.islower() else ord('A')
      shifted_letter = chr((ord(letter) - start + shift) % 26 + start)
    else:
      shifted_letter = letter
    result += shifted_letter
  return result

text = input("Type the message: ")
shifted_text = encrypt(text, 13)
print(shifted_text)
