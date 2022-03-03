#Write a program which uses map() and filter() to make a list whose elements are squares of even
#numbers in [1,2,3,4,5,6,7,8,9,10].
x=filter(lambda x:x%2==0,range(1,11))
#y=list(x)
y=map(lambda y:y**2,list(x))
print(list(y))
