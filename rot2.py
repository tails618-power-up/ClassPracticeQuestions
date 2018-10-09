def rot2(x):
    beginning=x[:2]
    end=x[2:]
    return end+beginning
word=input("What word would you like to disconfigure? ")
disconfigured=rot2(word)
print(disconfigured)
