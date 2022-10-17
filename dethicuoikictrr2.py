Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import itertools
>>> chars=['a','b','c','d','e','f','g','h','i','j']
>>> khonghieu=list(itertools.combinations(chars,5))
>>> import random
>>> u=random.randrange(len(khonghieu))
>>> ketqua=khonghieu[u]
>>> print(ketqua)
('b', 'c', 'f', 'g', 'i')
>>> pritn(ketqua)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    pritn(ketqua)
NameError: name 'pritn' is not defined
>>> print(ketqua)
('b', 'c', 'f', 'g', 'i')
>>> print(ketqua)
('b', 'c', 'f', 'g', 'i')
>>> ketqua=random.sample(chars,5)
>>> print(ketqua)
['e', 'c', 'a', 'b', 'f']
>>> ketqua=random.choice(chars,5)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ketqua=random.choice(chars,5)
TypeError: choice() takes 2 positional arguments but 3 were given
>>> ketqua=random.choice(chars,5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ketqua=random.choice(chars,5)
TypeError: choice() takes 2 positional arguments but 3 were given
>>> import itertools
>>> chars=['a','b','c','d','e','f','g','h','i','j']
>>> khonghieu=list(itertools.combinations(chars,5))
>>> import random
>>> u=random.randrange(len(khonghieu))
>>> ketqua=khonghieu[u]
>>> ketqua=random.choice(chars,5)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ketqua=random.choice(chars,5)
TypeError: choice() takes 2 positional arguments but 3 were given
>>> ketqua=random.randrange(len(chars),5)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ketqua=random.randrange(len(chars),5)
  File "C:\Users\ASUS\anaconda3\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (10, 5, -5)
>>> import itertools
>>> print(list(itertools.combinations_with_replacement('ABC')))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(list(itertools.combinations_with_replacement('ABC')))
TypeError: combinations_with_replacement() missing required argument 'r' (pos 2)
>>> print(list(itertools.combinations_with_replacement('ABC', 3)))
[('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'C', 'C'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'C', 'C'), ('C', 'C', 'C')]
>>> import numpy
i
>>> import scipy
>>> import numpy as np
>>> def alpha(a):
	return a+10

>>> def beta(b):
	return b*3

>>> def ham_hop(g,f):
	return (lambda x: g(f(x)))

>>> h=ham_hop(alpha,beta)
>>> h1)
SyntaxError: unmatched ')'
>>> print(h(1))
13
>>> import np
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    import np
ModuleNotFoundError: No module named 'np'
>>> import numpy
>>> for i1 in range(0,N):
	for i2 in range(i1,N):
		for i3 in range(i2,N):
			ketqua=ketqua+[{i1,i2,i3)]
			
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> for i1 in range(0,N):
	for i2 in range(i1,N):
		for i3 in range(i2,N):
			ketqua=ketqua+[(i1,i2,i3)]

			
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for i1 in range(0,N):
NameError: name 'N' is not defined
>>> (0,2,2) in ketqua
False
>>> (0,2,1) in ketqua
False
>>> A={'a','b','c','d'}
>>> B={'c','b','d','a','d'}
>>> A.equal(B)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    A.equal(B)
AttributeError: 'set' object has no attribute 'equal'
>>> import numpy
>>> A={'a','b','c','d'}
>>> B={'c','b','d','a','d'}
>>> A.equal(B)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    A.equal(B)
AttributeError: 'set' object has no attribute 'equal'
>>> numpy.equal(A,B)
True
>>> import itertools
>>> u=set(itertools.combinations_with_replacement('ABC',2))
>>> v=set(itertools.permutations('ABC',2))
>>> print(u)
{('B', 'C'), ('A', 'B'), ('C', 'C'), ('B', 'B'), ('A', 'C'), ('A', 'A')}
>>> print(v)
{('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'C'), ('B', 'A')}
>>> 