#Exercise 1

##letters_1 = {'D','E','F','G'}
##letters_2 = {'H','I'}
##
##letters_3 = letters_1.copy()
##print(letters_3)
##
##letters_1.add('I')
##letters_1.add('H')
##print(letters_1)
##
##letters_1.difference(letters_2)
##print(letters_1)
##
##letters_1.remove('I')
##print(letters_1)
##                             
##letters_1.discard('E')
##print(letters_1)
##
##print(len(letters_1))


#Exercise 2

##import collections
##months_Dq = collections.deque(['Mar','April','May'])
##
###appending right side
##months_Dq.append(['June','July','Aug'])
##print(months_Dq)
###appending left side
##months_Dq.appendleft(['Dec','Jan','Feb'])
##print(months_Dq)
##
##months_Dq.pop()
##print(months_Dq)
##
##months_Dq.popleft()
##print(months_Dq)
##
##months_Dq.remove("April")
##print(months_Dq)


#Exercise 3

##mile=[50,70,100]
##def miles_To_Km(num):
##    print ('Total km:{}'.format(num*1.6))
##
##miles_To_Km(sum(mile))


#Exercise 4

#module textinfo.py
##import textinfo as TI
##name= TI.upperCase("fox")
##print(name)


#Exercise 5

#module customer.py
##import customer as CM
##name = input("Enter your name: " )
##age = input("Enter your age: ")
##phone= input("Enter your phone number: ")
##maritial = input("Enter you maritial status: ")
##
##CM.name_verify(name)
##CM.age_verify(age)
##CM.phone_verify(phone)
##CM.maritial_verify(maritial)
##
##CM.store_info(name,age,phone,maritial)
##CM.r_info(name,age,phone,maritial)
##print("thank you")


#Exercise 6

##prod = {'tomato':'red','squash':'yellow','potato':'brown','avocado':'green'}
##def showProd(prod):
##    for i,j in prod.items():
##        print('{} :{}'.format(i,j))
##showProd(prod)
##print(locals())
##print(globals())


#Exercise 7
import Vendor as vd
db = {1:('laptop',299.99),2:('Gaming lapi',1029.99),3:('TV',249.99),4:('x-BOX ONE',219.99),5:('Nitendo switch',279.99)}
print('Here are the list of the products....')

for k,v in db.items():
    print ('{}) {} '.format(k,v[0], v[0]))

customer_list =[]
keep_choosing='y'
while keep_choosing == 'y':
    choice = int(input('\nWhat is your choice: '))

    if choice in db.keys():
        customer_list.append((db[choice][0],db[choice][1]))
    else:
        print("Invalid Option")

    keep_choosing = input('keep choosing (Y for yes, N for no)').upper()
vd.total(customer_list)
                 
              
