# while_loop =execute some code WHILE some condition remains true
# name = input("enter your name: ")
# while name == "":
#     print("you did not type your name")
#     name = input("Enter your name: ")
    
# print(f"hello {name}")

food = input("enter a food you like ( press q to quit): ")
while not food == "q":
    print(f"you like {food}")
    food = input("enter a food you like ( press q to quit): ")
    