Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.mkdir("e:\\internshala_test_dir")
>>> os.chdir("e:\\internshala_test_dir")
>>> os.getcwd()
'e:\\internshala_test_dir'
>>> os.chdir("e:\\")
>>> os.getcwd()
'e:\\'
>>> os.rmdir("e:\\internshala_test_dir")
>>> 
