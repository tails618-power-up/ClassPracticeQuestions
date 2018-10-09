def noFirstLastChar(s):
    s=s[1:-1]
    return s
word=input("What word would you like to murder? ")
printThing=noFirstLastChar(word)
print(printThing)
