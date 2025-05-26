fruits =["apple", "orange" , "banana", "coconut"]
vegetables = ["celery", "carrots","potatoes"]
meats = ["chicken", "fish", "turkey"]


groceries = [fruits,vegetables,meats]
# print(groceries)

for items in groceries:
    print(items)
    
for items in groceries:
    for item in items:
        print(item, end=" ")
    print()