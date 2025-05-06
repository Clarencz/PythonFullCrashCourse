import time

my_Time = int(input("Enter time in seconds: "))
for x in range(my_Time,0,-1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"00:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("time is up")