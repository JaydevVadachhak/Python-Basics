Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from MyFriends import food
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from MyFriends import food
ImportError: cannot import name 'food'
>>> from MyFriends import Food
>>> from MyFriends import Food
>>> from MyFriends import Food.food()
SyntaxError: invalid syntax
>>> food()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    food()
NameError: name 'food' is not defined
>>> Food.food()
Total of Amount:100
Total number of friends:2
50.0
>>> from MyFriends import Movie
>>> Movie.movie()
Total amount:5000
Total friends:10
500.0
>>> 
