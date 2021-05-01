age = 21

def global_fun():
    print("Global age printing:",globals()['age'])

    globals()['age'] = 22
    print("After updating global variables inside the block is",globals()['age'])

    age = 11
    print("this is local variable with same name as global variable",age)

global_fun()

print("global var value change checked",age)
