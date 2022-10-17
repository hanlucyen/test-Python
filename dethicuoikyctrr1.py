Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A={'a','b','c','c','d'}
>>> B={'c','b','d','a','d'}
>>> A==B
True
>>> equal(A,B)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    equal(A,B)
NameError: name 'equal' is not defined
>>> print(list(itertools.combinations_with_replacement('ABC', 3)))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(list(itertools.combinations_with_replacement('ABC', 3)))
NameError: name 'itertools' is not defined
>>> S=set()
>>> for i1 in range(0,3):
	for i2 range(i1,3):
		
SyntaxError: invalid syntax
>>> S=set()
>>> for i1 in range(0,3):
	for i2 in range(i1,3):
		for i3 in range(i2,N):
			S.add(i1*100+i2*10+i3)

			
Traceback (most recent call last):
  File "<pyshell#13>", line 3, in <module>
    for i3 in range(i2,N):
NameError: name 'N' is not defined
>>> S=set()
>>> for i1 in range(0,3):
	for i2 in range(i1,3):
		for i3 in range(i2,3):
			S.add(i1*100+i2*10+i3)

			
>>> S=set()
>>> for i1 in range(0,3):
	for i2 in range(i1,3):
		for i3 in range(i2,3):
			S.add(i1*100+i2*10+i3)
			print(S)

			
{0}
{0, 1}
{0, 1, 2}
{0, 1, 2, 11}
{0, 1, 2, 11, 12}
{0, 1, 2, 11, 12, 22}
{0, 1, 2, 11, 12, 111, 22}
{0, 1, 2, 11, 12, 111, 112, 22}
{0, 1, 2, 11, 12, 111, 112, 22, 122}
{0, 1, 2, 11, 12, 111, 112, 22, 122, 222}
>>> setA={n for n in range(100) if n % 2==1}
>>> setB={n for n in range(100) if n%2==0}
>>> setA<=setB
False
>>> setA!=setB
True
>>> setA>setB
False
>>> setA>setB
False
>>> x=9
>>> S=[2*x for x in range(1,x+1)]
>>> print(S)
[2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> for i1 in range(0,N):
	for i2 in range(i1,N):
		for i3 in range(i2,N):
			ketqua=ketqua+[(i1,i2,i3)]
			print(ketqua)

			
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    for i1 in range(0,N):
NameError: name 'N' is not defined
>>> for i1 in range(0,N):
	for i2 in range(i1,N):
		for i3 in range(i2,N):
			ketqua=ketqua+[(i1,i2,i3)]
			print(ketqua)

			
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for i1 in range(0,N):
NameError: name 'N' is not defined
>>> for i1 in range(0,N):
	for i2 in range(i1,N):
		for i3 in range(i2,N):
			ketqua=ketqua+[(i1,i2,i3)]

			
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for i1 in range(0,N):
NameError: name 'N' is not defined
>>> (0,2,2) in ketqua
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    (0,2,2) in ketqua
NameError: name 'ketqua' is not defined
>>> 
====================== RESTART: C:/Users/ASUS/Desktop/a.py ======================
Traceback (most recent call last):
  File "C:/Users/ASUS/Desktop/a.py", line 1, in <module>
    for i1 in range(0,N):
NameError: name 'N' is not defined
>>> 
====================== RESTART: C:/Users/ASUS/Desktop/a.py ======================
Traceback (most recent call last):
  File "C:/Users/ASUS/Desktop/a.py", line 4, in <module>
    ketqua=ketqua+[(i1,i2,i3)]
NameError: name 'ketqua' is not defined
>>> 
====================== RESTART: C:/Users/ASUS/Desktop/a.py ======================
Traceback (most recent call last):
  File "C:/Users/ASUS/Desktop/a.py", line 4, in <module>
    ketqua=ketqua+[(i1,i2,i3)]
NameError: name 'ketqua' is not defined
>>> 
====================== RESTART: C:/Users/ASUS/Desktop/a.py ======================
Traceback (most recent call last):
  File "C:/Users/ASUS/Desktop/a.py", line 4, in <module>
    ketqua=ketqua+[(i1,i2,i3)]
NameError: name 'ketqua' is not defined
>>> chars=['a','b','c','d','e','f','g','h','i','j']
>>> khonghieu=list(itertools.combinations(chars,5))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    khonghieu=list(itertools.combinations(chars,5))
NameError: name 'itertools' is not defined
>>> import numpy
>>> import scipy
>>> chars=['a','b','c','d','e','f','g','h','i','j']
>>> khonghieu=list(itertools.combinations(chars,5))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    khonghieu=list(itertools.combinations(chars,5))
NameError: name 'itertools' is not defined
>>> 