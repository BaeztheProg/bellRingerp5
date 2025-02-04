import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
special = list(string.punctuation)

def encrypt_caesar(message, shift):
  encrypted = ""
  
  for letter in message:
      for i, e in enumerate(lower):
          if e == letter:
              encrypted += lower[(i+shift)%len(lower)]
      for i, e in enumerate(upper):
          if e == letter:
              encrypted += upper[(i+shift)%len(upper)]
      for i, e in enumerate(special):
          if e == letter:
              encrypted += special[(i+shift)%len(special)]

message = 'Mr. Baez'
shift = 13

print(encrypt_caesar(message, shift))
