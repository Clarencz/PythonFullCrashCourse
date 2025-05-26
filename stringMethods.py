# name = input("Enter your full : ")
# phone_number = input("Enter your phone number: ")

# result = len(name)
# result = name.find("o") # first occurrence
# result = name.rfind("0") #find last
#name = name.capitalize() #capitalizes beginning of the name
# name = name.upper()
# result = name.isdigit()
#result = name.isalpha() #does not consider spaces as alphabetical
# result = phone_number.count("-")
# phone_number = phone_number.replace("-" ," ")


# print(help(str))

# print(name)
# print(phone_number)
# print(result)

##userName = input("Enter your fullName: ")
##if (len(userName) > 12 and userName.isdigit()):
##    print("userName should not be more than 12 character")
##elif not userName.find(" ") == -1:
##    print("userName should not have spaces")
##elif (userName.isalpha()):
##    print("userName can not contain numbers")
##else:
##    print(f"welcome {userName}")
##print(userName)
##
##result = userName.split(" ")
##print(result)

#replace
mySring = "i like apples"
print(mySring.replace("apples" , "oranges"))

#strip()
mycolor = "   i love red  "
print(mycolor.strip("i love"))
#join() - join all the iems in an iterable
word = " this is letter "
letters= [ "a","b","d","e"]
print(word .join(letters).split("letter"))
#isalnum() - checks for number and alphabet
