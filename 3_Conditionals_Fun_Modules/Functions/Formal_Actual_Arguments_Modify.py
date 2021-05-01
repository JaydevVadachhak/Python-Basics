def my_func(list):
    list.append(60)
    print("List accessed in function:","ID:",id(list),list)
    
mylist = [10,20,30]

print("Before passing to the function","ID:",id(mylist),mylist)

my_func(mylist)

print("after passing to the function","ID:",id(mylist),mylist)
