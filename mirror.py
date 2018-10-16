final=""
def mirror(x):
    global final
    length=len(x)
    length=int(length)
    full=x
    length1=length
    length2=length-1
    length3=length
    num1=length2
    num2=length3
    for i in range(length1):
        global final
        thing=full[num1:num2]
        num1-=1
        num2-=1
        final=final+thing
    return final
word=input("What word would you like to flip? ")
print(mirror(word))
