Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sayhello():
	print("Hi jaydev")
	return
KeyboardInterrupt
>>> type(sayhello)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(sayhello)
NameError: name 'sayhello' is not defined
>>> type(sayhello())
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(sayhello())
NameError: name 'sayhello' is not defined
>>> def sayhello():
	print("jaydev")

	
>>> 
>>> type(sayhello())
jaydev
<class 'NoneType'>
>>> type(sayhello)
<class 'function'>
>>> 
