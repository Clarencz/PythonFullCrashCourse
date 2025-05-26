fout = open('receipt.txt', 'w')
tax = 0.0775
def total(customer_list):
    subtotal = 0
    for i in customer_list:
        subtotal += (i[1])

    print(customer_list)
    print(f"Subtotal ${subtotal:.2f} ")
    shipping = subtotal * 0.05
    print(f"shipping ${shipping:.2f}")
    t_amount = tax * subtotal
    print(f"Tax: \t ${t_amount:.2f}")
    total = subtotal + t_amount + shipping
    print(f"Total: \t ${total:.2f}")
    receipt(customer_list, subtotal,total,shipping)

def receipt(customer_list,subtotal,total,shipping):
    fout.write('**** Receipt *****\n')
    fout.write('Item        Price\n')
    fout.write('----        -----\n')

    for i in customer_list:
        fout.write('{} ${}\n'.format(i[0],i[1]))

    fout.write('''
--------------------------------
Subtotal ${}
Shipping ${:.2f}
Tax      ${}
Total    ${:.2f}

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
Thank You For Shopping With us...
'''.format(subtotal,shipping,tax * 100,total))
fout.close()
print('\nYour Receipt has been printed')               
                
