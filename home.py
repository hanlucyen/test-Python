Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> print(math.pi)
3.141592653589793
>>> import sys
>>> sys.path
['', 'C:\\Users\\ASUS', 'C:\\Users\\ASUS\\anaconda3\\Scripts', 'C:\\Users\\ASUS\\anaconda3\\python38.zip', 'C:\\Users\\ASUS\\anaconda3\\DLLs', 'C:\\Users\\ASUS\\anaconda3\\lib', 'C:\\Users\\ASUS\\anaconda3', 'C:\\Users\\ASUS\\anaconda3\\lib\\site-packages', 'C:\\Users\\ASUS\\anaconda3\\lib\\site-packages\\locket-0.2.1-py3.8.egg', 'C:\\Users\\ASUS\\anaconda3\\lib\\site-packages\\win32', 'C:\\Users\\ASUS\\anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\Users\\ASUS\\anaconda3\\lib\\site-packages\\Pythonwin']
>>> def  outer_function():
	global a
	a=20

	
>>> def outer_function():
	global a
	a=20
	def inner_function():
		global a
		a=30
		print('a=',a)
	inner_function()
	print('a=',a)

	
>>> a=10
>>> outer_function()
a= 30
a= 30
>>> print('a=',a)
a= 30
>>> for val in sequence:
	loop body
	
SyntaxError: invalid syntax
>>> sum=0
>>> for val in numbers:
	sum=sum+val
	print(sum)

	
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    for val in numbers:
NameError: name 'numbers' is not defined
>>> print(sum)
0
>>> nember=[6,6,3,8,4,9,5,1]
>>> sum=0
>>> for val in number:
	sum=sum+val
print(sum)
SyntaxError: invalid syntax
>>> print(sum)
0
>>> print(range(10))
range(0, 10)
>>> pprint(range(0,10))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    pprint(range(0,10))
NameError: name 'pprint' is not defined
>>> digirs=[0,1,5]
>>> for i in digits:
	print(i)
	else:
		
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> diguts=[0,1,5]
>>> for i in digurs:
	print(i)

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for i in digurs:
NameError: name 'digurs' is not defined
>>> n=10
>>> sum=0
>>> i=1
>>> while i<=n:
	sum=sum+i
	i=i+1
print(sum)
SyntaxError: invalid syntax
>>> print(sum)
0
>>> n=10
>>> sum=0
>>> i=1
>>> while i<=n:
	sum=sum+i
	i=i+1#updte counter
#print the sum
>>>print("The sum is",sum)
SyntaxError: invalid syntax
>>> 
========================== RESTART: C:/Users/ASUS/c.py =========================
The sum is 55
>>> n=0
>>> sum=0
>>> i=1
>>> while i<=n:
	sum=sum+i
	i=i+1

	
>>> print(sum)
0
>>> for val in "string":
	if val =="i":
		beak

		
Traceback (most recent call last):
  File "<pyshell#75>", line 3, in <module>
    beak
NameError: name 'beak' is not defined
>>> for val in "string":
	if val=="i":
		break
	print(val)

	
s
t
r
>>> import scipy
>>> help(scipy)

>>> import scipy
>>> import scipy.interpolate
>>> def food():
	x=20
	def bar():
		global x
		x=25
	print('before calling bar:',x)
	print('calling bar now')
	bar()
	print('after calling bar:',x)

	
>>> dood()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    dood()
NameError: name 'dood' is not defined
>>> food()
before calling bar: 20
calling bar now
after calling bar: 20
>>> print(x)
25
>>> from turtle import *
>>> home()
>>> while True:
	rt(170)
	fd(200)

	
