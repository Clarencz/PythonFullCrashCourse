principle =  0
rate = 0
time = 0

while principle <= 0: #true
    principle = float(input("enter the principle amount"))
    if principle <=0 :
        print("principle can not be less than equal to zero")
        
while rate <= 0:
    rate = float(input("enter the principle amount"))
    if rate <=0 :
        print("principle can not be less than equal to zero")
        
while time <= 0:
    time = float(input("enter the principle amount"))
    if time <=0 :
        print("principle can not be less than equal to zero")
        
Amount  = principle * pow((1+rate/100),time)

print(f"you amount is ${Amount}")