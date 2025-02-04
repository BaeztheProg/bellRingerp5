def ceaserCipher(word):
  o = []
  c = []
  for each in word:
    value = ord(each)
    o.append(value)
  for i in range(0, len(o)):
    o[i] += 13
  for each in o:
    c.append(chr(each))
  return(c)
print(ceaserCipher(input("Type a string: ")))
