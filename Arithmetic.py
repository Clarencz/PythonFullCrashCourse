import math
# Arithmetic Operators

# friend = 0

# friend = friend + 1
# friend+= 3
# friend = friend - 1
# friend -= 1
# friend = friend * 2
# friend *= 2
# friend = friend / 2
# friend /= 2
# friend = friend // 2
# friend //= 2
# friend = friend % 2
# friend %= 2
# friend = friend ** 2
# friend **= 2

height = 45.5676
result = round(height)  # Rounds to the nearest integer
result = abs(height)
result = pow(2, 3)  # 2 raised to the power of 3
result = math.sqrt(16)  # Square root of 16
result = max(3,5,4,6)
result = min(4.2,3.5,4,3,4)
#sum() - adds the items of an iterable and returns the sum
vals = [1,2,3,4,5]
print(sum(vals,20))
print(result)
# print(f"{friend}")

#pow(x,y,z) x raised to y result % z
#finding the hypotnuse of a triangle
A = float(input("Enter the length of side A:"))
B = float(input("Enter the length of side B:"))
C = round(math.sqrt(pow(A,2) +pow(B,2)),2)
print(f"The length of the hypotenuse is {C}")
