#Write a function that accepts a string and prints the number of uppercase letters and lowercase
#letters.

# note: have not completed this code , throwing errors, not able to resolve the error

def string_test(s):
    count,total=0
    for i in s:
        
        if i.isupper():
                count+=1
        else:
                total+=1
    print("number of uppercase letters",count)
    print("number of lowercase letters",total)


string_test("HeLL0")