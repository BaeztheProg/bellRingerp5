list = ["M","r",".","B","a","e","z"]
list2 = ["N", "s", ".", "C", "b", "f", "a"]
def Caesar_Cipher():
  for i in range(len(list)):
    list[i] = list2[i]
  print(list)
  
Caesar_Cipher()
