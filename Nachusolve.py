re=input("pass")
cipher=13
newword=[]
for letter in re:
    if ord(letter)==(90):
        newword.append(chr(ord("a")+(cipher-1)))

    elif ord(letter)==(122):
        newword.append(chr(ord("A")+(cipher-1)))
    else:
        newword.append(chr(ord(letter)+cipher))


print(''.join(newword))
