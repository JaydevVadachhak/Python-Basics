n = int(input("Enter Number:"))
d=2
while n>1:
    if n%d==0:
       print(d)
       n=n/d
       continue
    d=d+1
