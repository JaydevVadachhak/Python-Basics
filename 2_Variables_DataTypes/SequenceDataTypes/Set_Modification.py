s1 = {"1","2","3"}
print(s1)
print("s1 add")
s1.add("4")
print(s1)


s2 = {"1","2"}
print(s2)
print("s2 updated")
s2.update("3","4")
print(s2)


s3={"1"}
print(s3)
print("S3 clear")
s3.clear()
print(s3)

s4={"1","2","3"}
print(s4)
print("s4 copied to s5")
s5=s4.copy()
print(s5)

s6={"1","2"}
print(s6)
print("s6 discard")
s6.discard("2")
print(s6)
s6.discard("3")
print(s6)


s7 = {"1","2"}
print(s7)
print("s7 remove")
s7.remove("2")
print(s7)

"""s7.remove("3")
print(s7)""" #this will give an error as it not contain 3
