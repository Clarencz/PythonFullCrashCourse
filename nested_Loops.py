#nested loops = a loop within another loop (outer, inner)
# outer loop:
#     inner loop:


# for x in range(3):
#     for y in range(1,10):
#         print(y, end ="")
#     print()

height  = int(input("Enter height: "))
width = int(input("Enter width: "))
symbol = input("Enter symbol to use: ")

for x in range(height):
    for y in range (width):
        print( symbol,end = "")
    print(x)