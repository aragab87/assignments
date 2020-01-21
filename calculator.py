#This script defines 4 functions for basic math operations

#Defines a function that takes two inputs: a and b, and returns a multiplied with b  
def multiply(a,b):
    return a * b

#Defines a function that takes two inputs: a and b, and returns a added to b  
def add(a,b):
    return a + b

#Defines a function that takes two inputs: a and b, and returns a minus b  
def subtract(a,b):
    return a - b

#Defines a function that takes two inputs: a and b, and returns a divded by b  
def divide(a,b):
    return a / b

#Defines a function that takes as input a, and returns a squared 
def square(a):
    return a ** 2

#Defines a function that takes an inputs: a , and returns a cubed 
def cube(a):
    return a ** 3

#Defines a function that takes an inputs: a and n, and returns 'a' squared n times.
def square_n(a,n):
    return a ** (2**n)



print("I'm going use the calculator functions to divide 5 and 2")
w = divide(5,2)
print(w)  

print("I'm going use the calculator functions to square 3")
x = square(3)
print(x)  

print("I'm going use the calculator functions to cube 3")
y = cube(3)
print(y) 

print("I'm going use the calculator functions to square 3 three times")
z = square_n(3,3)
print(z) 