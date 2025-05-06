#input = a function that allows the user to enter data from the keyboard

name = input("Enter your name: ")#prompts the user to enter their name
age = int(input("Enter your age: "))#prompts the user to enter their age
#input() returns a string, so we need to convert it to the appropriate data type

print(f"my name is {name} and i ama {age} years old")

print(type( age))

#Area of a Rectangle
length = float(input("Enter the length of the rectangle: "))#prompts the user to enter the length of the rectangle
width = float(input("Enter the width of the rectangle: "))#prompts the user to enter the width of the rectangle
area = length * width#calculates the area of the rectangle
print(f" the area is {area} square units")