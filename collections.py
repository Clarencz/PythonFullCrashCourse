#Collection = single "variable" used to store multiple values
#Lists = [] - ordered and changeable.Duplicates okay
#Set = {} - unordered and immutable, but Add/Remove OK. NO duplicates
#python contains two types of sets -mutable sets ,immutable frozenset

#Tuple = ()- ordered and unchangeable.Duplicates OK. FASTER


#LISTS

# fruits1 = ["apple","banana","orange"]
# #print(fruits[indexing])
# for fruit in fruits:
#     print(fruit)
    
# print(dir(fruits)) - shows all methods that can be used with Lists
# print(help(fruits)) - describes all the methods in detail
# del fruits1[2]
# fruits.extend()
# fruits.append()
# fruits.remove()
# fruits.reverse()
# fruits.sort()
# fruits.insert(0,"pineapple")
# fruits.index("banana")
# fruits.count("pineapple")
# fruits1.pop()
# print(fruits1)

# fruits = ["apple","banana","orange"]

#SETS

#    frozenset()- frozen sets can be used as keys in dictionary or as elements of another set, ut like sets it is not ordered(the elements can be set at any index)
#frozenset([iterable])
vowels = ('a','e','o','u')
fset = frozenset(vowels)
print(f'the frozen set is : {fset}')
print(f'the empty frozen set is {frozenset()}')
A = frozenset([1,2,3,4])
B = frozenset([3,4,5,6])
C = frozenset([5,6])

print(A.isdisjoint(C))
print(C.issubset(B))
print(B.issuperset(C))

C = A.copy()
print(C)

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

#mutable set methods
fruits = {"apple","banana","orange"}


print(dir(fruits))
print(help(fruits))

print(len(fruits))
print("pineapple" in fruits)
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()
fruits.update()
fruits.discard()
fruits
fruits.clear()

print(fruits)

#Tuples
fruits = ("apple","banana","orange")


print(dir(fruits))
print(help(fruits))

print(len(fruits))
print("pineapple" in fruits)
print(fruits.count("pineapple"))
print(fruits.index("apple"))


print(fruits)



#collections - the module called collections contains alternatives for these datatypes, high-performance specialized alternatives, in addition to a utility function for the creation of named tuples
# namedtuple(): will create a tuple for the creation of named tuples
#deques : provides lists that have fast appends and that pop at either end
# ChainMap: a class much like a dictionary that creates a single view showing multiple mappings for counting hashing objects
#OrderedDict : a dictionary subclass that will remember the order of entries
# a dictionary subclass that will call a function that can supply the missing values
# defaultdict : a dictionary subclass that will call a function that can supply the missing values
# UserDict, UserList, UserString : These datatypes sre used as wrappers for the base class that underlies each one.

#Deques - is a double-ended queue. These objects are similar to lists with support for appends that are thread-safe and memory efficient
#A deque - is mutable and has support for some of the list operations, like indexing, you can assign a deque by index, but you can not slice one directly
#using a deque instead of a list is that it is much faster to insert an item at the start of the start of a deque than it is at the start of the list.
#All deques are thread-safe and we can serialize them using a module called collections.perhaps one of the most useful ways to use a deque is for the population and consummationof items. Population and consummation of deque items happen sequentially from each end


import collections
DoubleEnded = collections.deque(["mon","tue","wed"])

#appending from right
print("adding to the right")
DoubleEnded.append("Thur")
print(DoubleEnded)

#append to the left
print("adding to the left:")
DoubleEnded.appendleft("sun")
print(DoubleEnded)

#Remove from the right
print("Removing from the right:")
DoubleEnded.pop()
print(DoubleEnded)

#Remove from the left
print("Removing from the left")
DoubleEnded.popleft()
print(DoubleEnded)

#Reverse the deque
print("Reversing the deque")
DoubleEnded.reverse()
print(DoubleEnded)
