from array import array

mylist = [1, 2, 3]
for item in mylist:
    print(item)

def add(x,y):
    if (type(x) is not type(y)): #checking type in python
        raise ValueError("operands should be the same type")
    elif (type(x) is str):
        raise ValueError("type string is not supported")
    print(type(x))
    print(type(y))
    return x+y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        raise ValueError('Cannot divide by zero')
    return x/y
def subtract(x,y):
    return x-y
print('raha salam')

def arraySample():
    mylist = [1,2,3]
    arr = array(mylist)
    """
    import numpy as np
    np.asarray(mylist)
    """
    for item in arr:
        print(item)
    return mylist[0]
