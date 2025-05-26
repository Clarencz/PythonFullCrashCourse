username = input("enter your name: ")
age = int(input("enter your age: "))


#Exercise 7
maxData = 750
Monthlycost = 100
userCons = int(input("Enter amount you need: "))
additionalStorage = userCons - maxData
additionalFee = additionalStorage * 5
totalCons = additionalFee + Monthlycost
print(f"monthly cst and additonal cost is, ${totalCons}")


#Exercise 19
customer_Purchase = 23
coffee_Beans = 10
customer_Purchase *= coffee_Beans
Discount = 0.10 * customer_Purchase
total_Cost = customer_Purchase - Discount
print(f"lisa your total cost is: ${total_Cost:.3f}")



