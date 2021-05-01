Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> float()
KeyboardInterrupt
>>> float(10)
10.0
>>> float(''1e-003)
SyntaxError: invalid syntax
>>> float('1e-003')
0.001
>>> float(''1e5)
SyntaxError: invalid syntax
>>> float('1e6')
1000000.0
>>> float('6=4j')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    float('6=4j')
ValueError: could not convert string to float: '6=4j'
>>> float('6+4j')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    float('6+4j')
ValueError: could not convert string to float: '6+4j'
>>> float(1e6)
1000000.0
>>> 
