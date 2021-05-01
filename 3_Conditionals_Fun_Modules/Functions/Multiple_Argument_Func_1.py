def verdict(m1,m2,m3):
    total = m1+m2+m3
    if total>=10000:
        print("You can buy smartphone")
    else:
        print("You havn't much money to buy smartphone")

gift = float(input("Enter gift money you got"))
saving = float(input("Saving money you have"))
pocket = float(input("pocketmoney you have"))

verdict(gift,saving,pocket)
