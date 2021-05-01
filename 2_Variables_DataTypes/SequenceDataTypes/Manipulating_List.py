l1 = ["Jaydev","55.90","9.7","90"]
print("list",l1)
l1.append(4+3j)
print("append",l1)

l1.insert(5,44)
print("insert at 5 index",l1)

l1.remove("55.90")
print("Item remove",l1)

l1.pop()
print("pop from list",l1)

l1.reverse()
print("ordered reverse",l1)

"""l1.sort()
print("sort",l1)"""

#this will give an error bcz, sort can't be done with diffrent data types like str and complex

print("\n")
l2 = [1,3,7,6,9,23,67,45]
l2.sort()
print("sort by ascending and alphanumeric",l2)
l2.sort(reverse=True)
print("sort by descending",l2)

