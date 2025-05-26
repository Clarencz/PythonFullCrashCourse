my_Name = "clarence"
print(len(my_Name))
print(my_Name[:4])
print(my_Name[1:])
print(my_Name[1:len(my_Name)])

#Exercise 2
##user_name ="Mabeyabear"
##user_age = "34"
##user_address = "111ngong"
##
##print(user_name.islower())
##print(user_name.startswith("j"))
##
##print(user_name.isalpha())
##print(user_name.isdigit())
##print(user_age.isdigit())
##print(user_address.isalnum())


#Exercise 3

##Nation = "Valhalla the land of Warriors"
##state = slice(8)
##state1 = slice(1,25,2)
##print(Nation[state])
##print(Nation[-8:])
##print(Nation[1:25:2])
##print(Nation[state1])

#Exercise 4

##Quote = "No Pain, no Gain!?!"
##Punctuations =["!", "?", ",",".","&"]
##for q in Quote:
##    if q in Punctuations:
##        Quote = Quote.replace(q,"")
##    print(Quote)

#Exercise 5

##Language = "PythonPython"
##s_first = Language[0:len(Language)//2]
##s_second = Language[len(Language)//2 if len(Language)%2 ==0 else((len(Language)//2)+1):]
##print(s_first)
##print(s_second)
#print(Language.split(Language//2))

#Exercise 6

##store1 = 400
##store2 = 530
##buy_TV = input("Enter the store to buy from:(store1 or store2) ")
##weight_TV = int(input("Enter the weight of the TV: "))
##cost_of_shipping = 1.25 * weight_TV               
##if buy_TV == "store1":
##    print (f"your TV  is worth ${store1} with free shipping")
##elif buy_TV == "store2":
##    print(f"your TV cost ${store2 + (cost_of_shipping)} includes shipping cost")
##else:
##    print("unknown store")


#Exercise 7

##total_weight_loss = 0
##weight_Loss_journey =[12,11.3,5,10]
##for weight in weight_Loss_journey:
##    total_weight_loss +=weight 
##    print(total_weight_loss)

#Exercise 8

Katie_orders = {"burger":9.99, "milkshake":5.25,"fries":2.75,"nachos":5.25,"lemonade":3.75}
total_cost = 0
##while not == "q":
##    for val in Katie_orders:
##        total_cost += Katie_orders[val]
##    print(total_cost)


#Exercise 9

student = [['jane','john','lamal','tokyo'],[22,23,24,25]]
for i in range(len(student)):
    for j in range(len(student[i])):
        print(student[i][j],end = ' ')
    print()
#Same as below    
for i, name in enumerate (student[0]):
    for j, age in enumerate (student[1]):
        if i == j :
            print(f"{name} : {age}")
# enumerate - function used in loops to get both the index and the value


#Exercise 10
children = ["Pablo","Leila","Jorge","Karla","Samuel"]
fullnames=[]
for name in children:
    fullnames.append(f"{name} Hernandez")
print(fullnames)

                  
#Exercise 11

year1_Savings = [200,320,180,210,175,305]
year2_Savings = [550,285,195,410]
totalyear1= 0
totalyear2 = 0
for amount in year1_Savings:
    totalyear1 += amount
    print(f'year1 total is {totalyear1}')
for amount in year2_Savings:
    totalyear2 += amount
    print(f"year2 total is {totalyear2}")
if totalyear1 > totalyear2:
    print("more saving in year1 than year2")
else:
    print("more savings in year 2 than in year1")
