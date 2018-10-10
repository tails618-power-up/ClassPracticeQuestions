from math import ceil
def extract(x):
    length=len(x)
    length=ceil(length/2)
    #length+=1
    beginning=x[:length-1]
    end=x[length:]
    return beginning+end
word=input("What word would you like to dissect? ")
print(extract(word))
