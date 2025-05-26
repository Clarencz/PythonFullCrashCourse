#Exception handling
#Finally- this is the action you will want to use to perform cleanup actions,whether the exceptions occur or not
#Assert  - condition that is going to trigger exception inside the code
#Raise - going to trigger an exception manually inside the code
#Try/except - this is when you want to block out a block of code and then it is recovered

#Example

#import module sys to get the type of exception
##import sys
##randomList = ['a',0,2]
##for entry in randomList:
##    try:
##        print("the entry is",entry)
##        r = 1/int(entry)
##        break
##    except:
##        print("ooop!",sys.exc_info()[0],"occurred")
##        print("Next entry.")
##        print()
##print(f"the reciprocal of entry, {entry} , is {r}")



#A try clause can have any number of except clause to handle different exceptions, however, only one will be executed in case an exception occurs
##try:
##    #do sth
##    pass
##except ValueError:
##    #handle ValueError exception
##    pass
##except (TypeError, ZeroDivisionError):
##    #handle multiple exceptions
##    #TypeError and ZeroDivisionError
##except:
##    #handle all other exceptions
##    pass

#Raising Exceptions
#exceptions are raised when error occur at runtime.we can also manually raise  exceptions using the keyword raise. We can optionally pass values to the exception to clarify why that exception was raised
##try:
##    print(1/0)
##except:
##    raise RuntimeError("something bad happened")

#Assert
#The Assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError
try:
    num = int(input("enter a number;"))
    assert num % 2 == 0
except:
    print("not an even number!")
else:
    reciprocal =1/num
    print(reciprocal)
#Try and Finally
# try statement optionally has the Finally clause. The clause is executed no matter what and is generally used to release external resources
#for eaxmple when connected to remote data center through the network or working with a file or GUI

#Example
f= open("test5.txt",'w')
f = open("test5.txt", 'r')
try:
    print('checking for errors')
except:
    f.readlines()
    f.close()
print('finish')

