#objecs and clsses
#object - is simply a collecion of data(varuables) an methods(functions) that act on thse data
#class is a blueprin of that object
#class definitions begin wih a class keyword
#A class creates a new local namespace where all is attributes are defined.Aribues may be data or functions

#there are also special attributes in it that begins with double underscores__. For example, __doc__ gives us he docstring of that class
#As soon as we define a class, anew class object with the same name. This class object allows us to access the different attributes as well as to instantiatet new objects of that class
#As many houses can be made from a house's blueprint, we can create many objects from a class. An object is also called an instance of a class and the process of creating this object called an instantiation

#Example:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Jane",30)
print(p1.name)
print(p1.age)

#the __init__() function is called automatically every time the class is being used to create a new object
#the self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
#the self parameter is areference to the current instance of the class, and it is used to access variables that belongs to the class
#self represents the instance of the class. By using the "self" keyword we can access the attributes of the class in python.It binds the attributes with the given arguments
#The reason you need to use self is because python does not use the @ syntax to refer to instance attributes.Python decided to do methods in a way that automatically, but not received automatically: the first parameter of methods is the instance the method is called on

#object methods
#objects can also contain methods.Methods in objects are functions that belong to the object

#Example:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name}")

p1= Person("jane",30)
p1.myfunc()

#updating object
#object can be reassigned with a different value
p1.age = 40
del p1
#self - is a parameter in function and user can use another parameter name in place of it. But it is advisable to use self because it increases the readability of the code
#Example:
##class this is a class:
##    def show(in place of self):
##        print("we have used another parameter name inplace of class")
##        
##object = this is a class()
##object.show()


class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color
    def show(self):
        print(f"Model is {self.model}")
        print(f"Color is {self.color}")

audi = Car("audi A4","blue")
ferrari = Car("ferrari 448","green")

audi.show()
ferrari.show()


#class attributes

class sampleClass:
    count= 0
    def increase(self):
        sampleClass.count +=1

s1= sampleClass()
s1.increase()
print(s1.count)

s2 = sampleClass()
s2.increase()
print(s2.count)

print(sampleClass.count)

#instance attributes
class emp:
    def __init__(self):
        self.name = 'xyz'
        self.salary = 4000
    def show(self):
        print(self.name)
        print(self.salary)
e1 = emp()
print("Dictionary form:", vars(e1))#return dictionary attributes
print(dir(e1))



        
    


