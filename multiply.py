#Write a program in Python to multiply the elements of a list by itself using a traditional function
#and pass the function to map() to complete the operation.


# 'int' object is not iterable what does this mean??
def multiply(lst):
    count=0
    for i in lst:
        i=i*i
        count+=1
x=map(multiply,[1,2,3])
print(list(x))
