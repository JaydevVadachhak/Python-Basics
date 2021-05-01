def phone(brand,ram):
    print(brand,ram)

##phone("Google")
##this will give error bcz it has only one argument although we define two argument
##in function

##phone(6,"Google")
##this will also give an error bcz data type changed in calling this function

phone(ram=6,brand="Google")
