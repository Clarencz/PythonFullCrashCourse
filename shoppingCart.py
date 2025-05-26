foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(Q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price {food}: $"))
        foods.append(food)
        prices.append(price)

print("------------Your Shopping..............")
for food,price in zip(foods,prices):
    print(f"{food} - {price:^6}")
    total += price
print(f"Total to pay: {total}")

