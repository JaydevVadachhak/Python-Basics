def verdict(m1,m2,m3,m4=10000):
    total = m1+m2+m3
    if total>=m4:
        print("You can buy smartphone")
    else:
        print("You havn't much money to buy smartphone")

gift = float(input("Enter gift money you got"))
saving = float(input("Saving money you have"))
pocket = float(input("pocketmoney you have"))

verdict(gift,saving,pocket,20000)

