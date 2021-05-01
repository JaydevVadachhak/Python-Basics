l1 = ["1","jaydev",55,60.5]
l2 = ["55.90","Jay",4+3j]
print(l1)
print(l2)
print(l1+l2)

print("\n")

t1 = ("1",5+5j,90.56,"jay")
t2 = ("jaydev",60.70,"khushi",12.34)
print(t1)
print(t2)
print(t1+t2)

print("\n")
print(l1*3)
print(t2*5)

print("\n")
print(l1[2])
print(l1[-2])
print(t2[-2])
print(t1[2])

print("\n")
print(l1[:3])
print(l2[1:3])
print(t1[2:])

print("\n")
print("2" in l1)
print(2 in l2)
print(4+3j in l2)

print("\n")
print("1" not in t1)
print(60.70 not in t1)
