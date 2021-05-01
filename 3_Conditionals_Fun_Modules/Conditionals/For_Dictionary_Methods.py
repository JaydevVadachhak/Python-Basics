names = {"Jaydev":"JD","Dipak":"DI","Khushi":"KH"}

print(names)

print("\n")

for x in names.items():
    print(x)

print("\n")

for x in names.keys():
    print(x)

print("\n")

for x in names.values():
    print(x)

print("\n")

for x in names.keys():
    print("the nick name of {} is {}".format(x,names.get(x)))
