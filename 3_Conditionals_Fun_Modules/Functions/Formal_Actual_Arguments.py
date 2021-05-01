def my_func(list):
    print("List accessed in function:","ID:",id(list))
    
mylist = [10,20,30]

print("Before passing to the function","ID:",id(mylist))

my_func(mylist)
