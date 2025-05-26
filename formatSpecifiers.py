# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify 
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

#POINT TO NOTE WHEN USING FORMAT SPECIFIERS SUCH AS THE :^ DO NOT FORGET TO INCLUDE WITH HOW MANY SPACES DO YOU INTEND TO ALIGN OR SHIFT THE VALUE EG :^6 WHICH MEANS IT SHIFT THE VALUE 6SPACES (WIDTH)

price1 = 34.23
price2 = -345.23
price3 =  34.11

print(f"price 1 is ${price1:010.1f}")


ship_rate = 2.66
tablet_weight = 1
laptop_weight = 7
tv_weight = 37

ship_tablet = tablet_weight * ship_rate
print(f"shipping amount of tablet is: ${ship_tablet:.2f}")
