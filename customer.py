def name_verify(name):
    if name.isalpha():
        print(name)
    else:
        input("enter a valid name")

def age_verify(age):
    if age.isdigit():
        print(age)
    else:
        input("enter a valid age")

def phone_verify(phone):
    if phone.isdigit():
        print(phone)
    else:
        input("enter a valid phone number")

def maritial_verify(maritial):
    if maritial.isalpha():
        print(maritial)
    else:
        input("enter a valid maritial status")

def store_info(name,age,phone,maritial):
    file = open('customerinfo.txt','w')
    file.write(name + '\n')
    file.write(age + '\n')
    file.write(phone + '\n')
    file.write(maritial + '\n')
    file.close()
    print('Information stored')

def r_info(name,age,phone,maritial):
    file=open('customerinfo.txt','r')
    print(file.read())
    file.close()
