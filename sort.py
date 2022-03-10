#Write a program that accepts a hyphen-separated sequence of words as input and prints the words
#in a hyphen-separated sequence after sorting them alphabetically.


def sort(seq):
    words=seq.split('-')
    words.sort()
    for word in words:
       # print(word.capitalize())
        print('-'.join(words))
       
sort("hello-world-there")


