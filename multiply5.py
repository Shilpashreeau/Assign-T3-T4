#Create a list of elements such that it contains the squares of the first and last 5 elements between
#1 and30 (both included).
lst=[]
for i in range(1,31):
    lst.append(i)

lst1=lst[0:5]
print(lst1)
lst3=[]
for x in lst1:
    x=x**2
    lst3.append(x)
print(lst3)


lst2=lst[-5:]
print(lst2)
lst4=[]
for y in lst2:
    y=y**2
    lst4.append(y)
print(lst4)
