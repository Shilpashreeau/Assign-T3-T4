#Write a program that accepts a hyphen-separated sequence of words as input and prints the words
#in a hyphen-separated sequence after sorting them alphabetically.

#note: I didnt get this code. I am not able to find the solution

def sort(seq):
    words=seq.split()
    words.sort()
    for word in words:
        print(word.capitalize())
       
sort("hello-world-there")


