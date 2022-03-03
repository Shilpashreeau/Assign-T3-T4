#Create a function that takes a list and returns a new list with unique elements of the first list.
# have done this two ways:
def unique(lst):
    return set(lst)

y=unique([1,2,3,1,4,2])
print(list(y))

def unique(lst):
    y=set(lst)
    return list(y)
x=unique([1,1,2,2,3,4]) 
print(x)