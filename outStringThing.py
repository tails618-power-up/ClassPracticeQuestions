string="-><-"
def outString(x):
    global string
    return string[:2]+x+string[2:]
word=input("What word would why would when what worm? ")
print(outString(word))
