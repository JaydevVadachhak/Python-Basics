Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Inheritance.py 
>>> q1 = Quadrilateral(1,1,1,1)
>>> q1.Perimeter()
4
>>> 

>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Inheritance.py 
>>> r1 = Rectangle(10,20)
>>> r1.Perimeter()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    r1.Perimeter()
  File "E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Inheritance.py", line 8, in Perimeter
    perimeter = self.side1 + self.side2 + self.side3 + self.side4
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Inheritance.py 
>>> r1 = Rectangle(10,20)
>>> r1.Perimeter()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    r1.Perimeter()
  File "E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Inheritance.py", line 8, in Perimeter
    perimeter = self.side1 + self.side2 + self.side3 + self.side4
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Inheritance.py 
>>> r1 = Rectangle(10,20)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    r1 = Rectangle(10,20)
  File "E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Inheritance.py", line 13, in __init__
    super().__init__(a,b,c,d)
NameError: name 'c' is not defined
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Inheritance.py 
>>> r1 = Rectangle(10,20)
>>> r1.Perimeter()
60
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Overriding.py 
Rajesh is 9000
Traceback (most recent call last):
  File "E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Overriding.py", line 20, in <module>
    s1 = SalesOfficer("jaydev",12000,1000)
NameError: name 'SalesOfficer' is not defined
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T03-Understanding Inheritance/Overriding.py 
Rajesh is 9000
jaydev is 13000
>>> 
