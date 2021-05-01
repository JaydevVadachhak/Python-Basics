s1 = {"1","2","3"}
s2 = {"1","4","5","6"}

print("Set 1",s1)
print("Set 2",s2)

print("\n")
print("Uninon")
print("Method 1 (s1|s2)")
print(s1|s2)
print("Method 2 (s1.union(s2))")
print(s1.union(s2))

print("\n")
print("Intersection")
print("Method 1 (s1&s2)")
print(s1&s2)
print("Method 2 (s1.intersection(s2))")
print(s1.intersection(s2))

print("\n")
print("Difference")
print("Method 1 (s1-s2) or (s2-s1)")
print((s1-s2),(s2-s1))
print("Method 2 (s1.difference(s2) or (s2.difference(s1))")
print((s1.difference(s2)),(s2.difference(s1)))

print("\n")
print("Symmetric Diference")
print("Method 1 (s1^s2) or (s2^s1)")
print((s1^s2),(s2^s1))
print("Method 2 (s1.symmetric_difference(s2)) or (s2.symmetric_difference(s1))")
print((s1.symmetric_difference(s2)),(s2.symmetric_difference(s1)))
