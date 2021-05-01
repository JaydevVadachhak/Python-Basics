num = int(input("Enter any number: "))
fact = 1

for x in range(1,num+1):
    fact = fact*x;
print("Factorial of {:d} is {:f}".format(num,fact))
