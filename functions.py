#def keyword marks the start of a function header
#function name uniquely identifies a function. Function nameing follows rules of writing identifiers in python
#parameters through which we pass  to a function.They are optional .
#colon(:) to mark the end of the function header
# optional documentation string(docstring) to describe what the function does
#one or more valid python statements that make up the function body. Statements must have the same indentation level
#optional return statement to return a value from the function
#syntax:

##def function_name(parameters):
##    '''docstring'''
##    statement(s)

# example
name = input("enter your name: ")
def greet():
    print(f"Hello, {name}")

greet()

#Example of returning value from a function
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num
print(absolute_value(2))
print(absolute_value(-4))

#using multiple arguments
def calculateSum(*args):
    totalSum= 0
    for num in args:
        totalSum += num
    print(totalSum)
calculateSum(3,2,4,23,1)

#using variable  number of keyword arguments passed
def displayArgument(**kwargs):
    for arg in kwargs.items():
        print(arg)

displayArgument(argument1 = 'hello', argument2 = 4,argument3= "Hi")


#Example
user_Age = int(input("enter your age: "))
def checkAge(user_Age):
    if user_Age < 65:
        print("you are under 65")
    else:
        print("your age is 65 or higher")

checkAge(user_Age)

#Example
num = int(input("Enter a number:"))
def ev_odd(num):
    print("even" if num % 2 == 0  else "odd")

ev_odd(num)

#Global Variables - utilised as amultipurpose variable used in any part of python
#Local Variables - declared within a python funtion or a module and is utilized solely in a specific program or python module
#python has two inbuilt methods named globals() and locals() - they allow you to determine whether a variable is either part of the global namespace or the local namespace

def fun():
    var =123
    print('locals:', locals())
    print('vars:', vars())
    print('Globals:', globals())
fun()
    
        
    
    
