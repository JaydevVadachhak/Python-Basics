total = 0
numbers = [1,2,3,4,5]

for num in numbers:
    total = total + num
avg = total/len(numbers)
print("the average of {} is {}".format(numbers,avg))
