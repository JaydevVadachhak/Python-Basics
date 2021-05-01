year = int(input("Enter any Year:"))

if year<0:
    print("Year Entry is not valid")
elif year%100==0:
    if year%400==0:
        print("Year is Leap Year")
    else:
        print("Year is Not Leap Year")
else:
    if year%4==0:
        print("Year is Leap Year")
    else:
        print("Year is Not Leap Year")
