# dictionary - unordered collection of items. Each item of a dictionary has  KEY/VALUE pair identified by use of curly braces {}
# values can be of any data type and can repeat, keys must be of immutable type {string,number or tuple with immutable elements} and must be unique
# while indexing is used with other data types to access values, a dictionary uses keys. Keys can be used either inside square brackets [] or with the get() method

dict1 = {"name":"julie","age":23}
print(dict1["age"])
print(dict1.get("name"))
dict1["address"]="Downtown"
print(dict1)


#dict1.pop("address") - remove specified key
#dict1.popitem() - remove last item in the directory

print(dir(dict1))

#Dictionary Comprehension - consist of an expression pair (key:value) followed by a for statement inside curly braces {}
#A dictionary comprehension can optionally contain more for or if statements
#An optional if statement can filter out items to form the new dictionary

squares = {x :x for x in range(6)}
print(squares)

#same as:
squares ={}
for x in range(6):
 squares[x] = x*x
print(squares)
