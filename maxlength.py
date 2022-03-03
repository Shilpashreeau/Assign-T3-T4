#7. Define a function that can accept two strings as input and print the string with the maximum length
#in the console. If two strings have the same length, then the function should print both the strings line
#by line.
def maxlen(a,b):
    if len(a)>len(b):
        print(a)
    elif len(b)>len(a):
        print(b)
    else:
        print(a)
        print(b)
      

maxlen('hi','hello')