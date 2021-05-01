Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T04-Using Magic Methods/__add__.py 
>>> d1 = Distance(7,8)
>>> d2 = Distance(9,25)
>>> d3 = d1 + d2
>>> d3
<__main__.Distance object at 0x01606CB0>
>>> 
 RESTART: E:/internshala/Programming With Python/M4/4-Principles of Object-oriented Programming (OOP)/T04-Using Magic Methods/__add__.py 
>>> d1 = distance(9,20)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d1 = distance(9,20)
NameError: name 'distance' is not defined
>>> d1 = Distance(9,20)
>>> d2 = Distance(20,50)
>>> d3 = d1 + d2
>>> print(d3)
Distance:30feet and58inches
>>> 
