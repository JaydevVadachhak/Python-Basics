Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> int(10)
10
>>> int(-10)
-10
>>> int(10.55)
10
>>> int(-458.63)
-458
>>> int(0.52)
0
>>> int('11')
11
>>> int("56.2")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int("56.2")
ValueError: invalid literal for int() with base 10: '56.2'
>>> int('12',8)
10
>>> int('8',8)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int('8',8)
ValueError: invalid literal for int() with base 8: '8'
>>> print('10',12)
10 12
>>> int('10',12)
12
>>> 
=============================== RESTART: Shell ===============================
>>> float(10)
10.0
>>> float('10.45')
10.45
>>> float('1e-003')
0.001
>>> float('1E6')
1000000.0
>>> float(1E6)
1000000.0
>>> 
