print("Squats Average")

day=0
squats=0
total=0

while day<=6:
    day=day+1
    squats = int(input("Enter squats on day {}:".format(day)))
    total=total+squats
avg=total/day
print("Average Squats:",avg)
