def last_two(s):
    #do the work
    s1=s[-2:]
    output=s1*3
    return output
if last_two("hello")=="lololo":
    print("Correct")
else:
    print("Incorrect")
if last_two("Hi")==="HiHiHi":
    print("Correct")
else:
    print("Incorrect")
