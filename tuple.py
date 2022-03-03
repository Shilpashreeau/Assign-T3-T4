#Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).
def square(a,b):
    lst=[]
    for i in range(a,b):
        i=i**2
        lst.append(i)
    print(tuple(lst))
        
 # i have a doubt here without setting limit to 21 can we do in any other ways??   
square(1,21)



