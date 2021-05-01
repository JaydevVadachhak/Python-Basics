Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T02-Declaring Class and Creating Objects/person.py 
>>> p1 = person()
>>> p1.ShowInfo()
Jaydev
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T02-Declaring Class and Creating Objects/person_1.py 
>>> p1 = person('Jaydev','22')
>>> p1.ShowInfo()
Name: Jaydev
gender: 22
>>> p2 = person('Khushi','30')
>>> p2.ShowInfo()
Name: Khushi
gender: 30
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T02-Declaring Class and Creating Objects/person_2.py 
>>> p1 = pesron('1','10')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    p1 = pesron('1','10')
NameError: name 'pesron' is not defined
>>> p1 = person('Jaydev','50')
>>> p1 = person('khushi','20')
>>> p3 = person('yash','20')
>>> p4 = person('nikhil','50')
>>> person.ShowCount()
No of objects so far: 4
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T02-Declaring Class and Creating Objects/Quiz_1.py 
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T02-Declaring Class and Creating Objects/Quiz_1.py 
>>> h1 = cupcake('cherry')
anything
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T02-Declaring Class and Creating Objects/Quiz_1.py 
>>> h1 = cupcake
KeyboardInterrupt
>>> h1 = cupcake('cherry')
anything: cherry
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T02-Declaring Class and Creating Objects/car_1.py 
>>> c1 = car()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c1 = car()
TypeError: __init__() missing 1 required positional argument: 'a'
>>> c1 = car(40)
>>> c1.get_speed()
40
>>> c1.set_speed(80)
>>> c1.get_speed()
80
>>> 
