program_running = True
while program_running == True:
  encrypted_message = ""
  letter_list = "abcdefghijklmnopqrstuvwxyz"
  caesar_input = input("Input the message you want to encrypt here: > ")
  move_by = input("Shifted over by how much? > ")
  for char in caesar_input:
    for letter in letter_list:
      if letter.upper() == char.upper():
        try:
          encrypted_message += letter_list[letter_list.index(letter)+int(move_by)]
        except IndexError: 
          new_letter = char
          new_count = 0
          add_by = 0
          reset_order = True
          index = letter_list.index(letter)
          while add_by < (int(move_by)):
            try:
              new_letter = letter_list[letter_list.index(letter)+add_by]
            except IndexError:
              reset_order = False
              new_letter = letter_list[new_count + 1]
              new_count += 1
            add_by += 1
          new_count = 0
          encrypted_message += new_letter
  print(encrypted_message)
  continueAgain = input("Do you want to continue? > \n [Y] \n [N] \n")
  if "y" in continueAgain.lower():
    continue
  elif "n"in continueAgain.lower():
    break;
  else:
    continue
