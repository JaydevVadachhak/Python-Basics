n = int(input("Enter number:"))

for x in range(2,n+1):
    if n%x==0:
        print(x)
        n=n/x
    x=x+1 
