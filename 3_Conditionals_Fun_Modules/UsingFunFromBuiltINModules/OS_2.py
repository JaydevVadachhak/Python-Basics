Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.listdir("e:\\internshala")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    os.listdir("e:\\internshala")
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'e:\\internshala'
>>> os.listdir("e:\\internsala")
['business communication skills', 'digital markting', 'Programming With Python']
>>> 
