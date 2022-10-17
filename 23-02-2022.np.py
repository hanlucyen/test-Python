Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> a= np.array([1,4,5,8],float)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a= np.array([1,4,5,8],float)
NameError: name 'np' is not defined
>>> from numpy import *
>>> a=np.array([1,4,5,8],float)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a=np.array([1,4,5,8],float)
NameError: name 'np' is not defined
>>> import numpy as np
>>> a=np.array([1,4,5,8],float)
>>> a
array([1., 4., 5., 8.])
>>> type(a)
<class 'numpy.ndarray'>
>>> a[:2]
array([1., 4.])
>>> a[3]
8.0
>>> a[0]=5
>>> a
array([5., 4., 5., 8.])
>>> a=np array([1,2,3],[4,5,6],float)
SyntaxError: invalid syntax
>>> a=np.array([1,2,3],[4,5,6],float)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a=np.array([1,2,3],[4,5,6],float)
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
>>> a=np.array([[1,2,3],[4,5,6]],float)
>>> a
array([[1., 2., 3.],
       [4., 5., 6.]])
>>> a[0,0]
1.0
>>> a[0,1]
2.0
>>> a=np.array([[1,2,3],[4,5,6]],float)
>>> a[1,:]
array([4., 5., 6.])
>>> len(a)
2
>>> 2 in a
True
>>> 0 in a
False
>>> a=np.array(range(10),float)
>>> a
array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
>>> a=a.reshape((5,2))
>>> a
array([[0., 1.],
       [2., 3.],
       [4., 5.],
       [6., 7.],
       [8., 9.]])
>>> a.shape
(5, 2)
>>> a=np.array([1,2,3],float)
>>> b=a
>>> c=a.copy()
>>> a[0]=0
>>> a
array([0., 2., 3.])
>>> b
array([0., 2., 3.])
>>> c
array([1., 2., 3.])
>>> a=np.array([1,2,3],float)
>>> a.tolist()
[1.0, 2.0, 3.0]
>>> list(a)
[1.0, 2.0, 3.0]
>>> a=array([1,2,3],float)
>>> s=a.tostring()

Warning (from warnings module):
  File "<pyshell#39>", line 1
DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
>>> s=a.tostring()
>>> s
b'\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'
>>> np.fromstring(s)

Warning (from warnings module):
  File "<pyshell#42>", line 1
DeprecationWarning: The binary mode of fromstring is deprecated, as it behaves surprisingly on unicode inputs. Use frombuffer instead
array([1., 2., 3.])
>>> a=array([1,2,3],float)
>>> a
array([1., 2., 3.])
>>> a.fill(0)
>>> a
array([0., 0., 0.])
>>> a=np.array([[1,2,3],[4,5,6]],float)
>>> a
array([[1., 2., 3.],
       [4., 5., 6.]])
>>> a=np.array(rang(6),float).reshape((2,3))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a=np.array(rang(6),float).reshape((2,3))
NameError: name 'rang' is not defined
>>> a=np.array(range(6),float).reshape((2,3))
>>> a
array([[0., 1., 2.],
       [3., 4., 5.]])
>>> a.transpose()
array([[0., 3.],
       [1., 4.],
       [2., 5.]])
>>> a=np.array([[1,2,3],[4,5,6]],float)
>>> a
array([[1., 2., 3.],
       [4., 5., 6.]])
>>> a.flatten()
array([1., 2., 3., 4., 5., 6.])
>>> a=np.array([1,2],float)
>>> b=np.array(3,4,5,6],float)
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> a=np.array([1,2],float)
>>> b=np.array([3,4,5,6],float)
>>> c=np.array([7,8,9],float)
>>> np.concatenate((a,b,c))
array([1., 2., 3., 4., 5., 6., 7., 8., 9.])
>>> a=array([[1,2],[3,4]],float)
>>> b=np.array([[5,6],[7,8]],float)
>>> np.concatenate((a,b))
array([[1., 2.],
       [3., 4.],
       [5., 6.],
       [7., 8.]])
>>> np.concatenate((a,b),axis=0)
array([[1., 2.],
       [3., 4.],
       [5., 6.],
       [7., 8.]])
>>> np.concatenate((a,b),axis=1)
array([[1., 2., 5., 6.],
       [3., 4., 7., 8.]])
>>> a=np.array([1,2,3],float)
>>> a
array([1., 2., 3.])
>>> a[:np.newaxis]
array([1., 2., 3.])
>>> a[:,np.newaxis]
array([[1.],
       [2.],
       [3.]])
>>> b[np.newaxis,:]
array([[[5., 6.],
        [7., 8.]]])
>>> b[np.nrwaxis,:].shape
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    b[np.nrwaxis,:].shape
  File "C:\Users\ASUS\anaconda3\lib\site-packages\numpy\__init__.py", line 303, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'nrwaxis'
>>> b[np.newaxis,:].shape
(1, 2, 2)
>>> np.arange(5,dtype=float)
array([0., 1., 2., 3., 4.])
>>> np.arange(1,6,2,dtype=int)
array([1, 3, 5])
>>> np.ones((2,3),dtype=float)
array([[1., 1., 1.],
       [1., 1., 1.]])
>>> np.seros(7,dtype=int)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    np.seros(7,dtype=int)
  File "C:\Users\ASUS\anaconda3\lib\site-packages\numpy\__init__.py", line 303, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'seros'
>>> np.seros((2,3),dtype=float)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    np.seros((2,3),dtype=float)
  File "C:\Users\ASUS\anaconda3\lib\site-packages\numpy\__init__.py", line 303, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'seros'
>>> a=np.array([1,2,3],float)
>>> a
array([1., 2., 3.])
>>> a[:,np.newaxis]
array([[1.],
       [2.],
       [3.]])
>>> n[:,np.newaxis].shape
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    n[:,np.newaxis].shape
NameError: name 'n' is not defined
>>> a[:,np.newaxis].shape
(3, 1)
>>> b[np.newaxis,:].shape
(1, 2, 2)
>>> b[:,np.newaxis]
array([[[5., 6.]],

       [[7., 8.]]])
>>> b[np.newaxis,:]
array([[[5., 6.],
        [7., 8.]]])
>>> np.arange(5,dtype=float)
array([0., 1., 2., 3., 4.])
>>> np.arange(1,6,2,dtype=int)
array([1, 3, 5])
>>> np.ones((2,3),dtype=float)
array([[1., 1., 1.],
       [1., 1., 1.]])
>>> np.seros(7,dtype=int)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    np.seros(7,dtype=int)
  File "C:\Users\ASUS\anaconda3\lib\site-packages\numpy\__init__.py", line 303, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'seros'
>>> np.zeros(7,dtype=int)
array([0, 0, 0, 0, 0, 0, 0])
>>> a=np.array([[1,2,3],[4,5,6]],float)
>>> np.zeros_like(a)
array([[0., 0., 0.],
       [0., 0., 0.]])
>>> np.ones_like(a)
array([[1., 1., 1.],
       [1., 1., 1.]])
>>> np.identity(4,dtype=float)
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
>>> np.eye(4,k=1,dtype=float)
array([[0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.],
       [0., 0., 0., 0.]])
>>> a=np.array([1,2,3],float)
>>> b=np.array([5,2,6],float)
>>> a+b
array([6., 4., 9.])
>>> a-b
array([-4.,  0., -3.])
>>> a*b
array([ 5.,  4., 18.])
>>> b/a
array([5., 1., 2.])
>>> a%b
array([1., 0., 3.])
>>> b**a
array([  5.,   4., 216.])
>>> a=np.array([[1,2],[3,4]],float)
>>> b=np.array([[2,0],[1,3]],float)
>>> a*b
array([[ 2.,  0.],
       [ 3., 12.]])
>>> a=np.array([1,2,3],float)
>>> bnp.array([4,5],float)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    bnp.array([4,5],float)
NameError: name 'bnp' is not defined
>>> b=np.array([4,5],float)
>>> a*b
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a*b
ValueError: operands could not be broadcast together with shapes (3,) (2,) 
>>> a+b
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a+b
ValueError: operands could not be broadcast together with shapes (3,) (2,) 
>>> a=np.array([1,2,3],float)
>>> b=np.array([4,5],float)
>>> a+b
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a+b
ValueError: operands could not be broadcast together with shapes (3,) (2,) 
>>> a=np.array([[1,2],[3,4],[5,6]],float)
>>> b=np.array([-1,3],float)
>>> a
array([[1., 2.],
       [3., 4.],
       [5., 6.]])
>>> b
array([-1.,  3.])
>>> a+b
array([[0., 5.],
       [2., 7.],
       [4., 9.]])
>>> a=np.zeros((2,2),float)
>>> b=np.array([-1.,3.],float)
>>> a
array([[0., 0.],
       [0., 0.]])
>>> b
array([-1.,  3.])
>>> a+b
array([[-1.,  3.],
       [-1.,  3.]])
>>> a+b[np.newaxis,:]
array([[-1.,  3.],
       [-1.,  3.]])
>>> a+b[:,np.newaxis]
array([[-1., -1.],
       [ 3.,  3.]])
>>> np.sqrt(a)
array([[0., 0.],
       [0., 0.]])
>>> a=np.array([1,4,9],float)
>>> np.sqrt(a)
array([1., 2., 3.])
>>> a=np.array([1.1,1.5,1.9],float)
>>> np.floor(a)
array([1., 1., 1.])
>>> np.ceil(a)
array([2., 2., 2.])
>>> np.rint(a)
array([1., 2., 2.])
>>> np.pi
3.141592653589793
>>> np.e
2.718281828459045
>>> a=np.array([1,4,5],int)
>>> for x in a:
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> a=np.array([1,4,5],int)
>>> for x in a:
	print x<hit return>
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x<hit return>)?
>>> for x in a:
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> a=np.array{[1,2],[3,4],[5,6],float)
SyntaxError: invalid syntax
>>> a=np.array([1,2],[3,4],[5,6],float)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    a=np.array([1,2],[3,4],[5,6],float)
TypeError: array() takes from 1 to 2 positional arguments but 4 were given
>>> a=np.array([[1,2],[3,4],[5,6]],float)
>>> for x in a:
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> a=np.array([2,4,3],float)
>>> a.sum()
9.0
>>> a.prod()
24.0
>>> a=np.array([2,1,9],float)
>>> a.mean()
4.0
>>> a.var()
12.666666666666666
>>> a.std()
3.559026084010437
>>> a=np.array([2,1,9],float)
>>> a.min()
1.0
>>> a.max()
9.0
>>> a.argmin()
1
>>> a.argmax()
2
>>> a=np.array([[0,2],[3,-1],[3,5]],float)
>>> a.mean(axis=0)
array([2., 2.])
>>> a.mean(axis=1)
array([1., 1., 4.])
>>> a.min(axis=0)
array([ 0., -1.])
>>> a.min(axis=1)
array([ 0., -1.,  3.])
>>> a.max(axis=0)
array([3., 5.])
>>> a=np.array([6,2,5,-1,0],float)
>>> sorted(a)
[-1.0, 0.0, 2.0, 5.0, 6.0]
>>> a.sort()
>>> a
array([-1.,  0.,  2.,  5.,  6.])
>>> a=np.array([6,2,5,-1,0],float)
>>> a.clip(0,5)
array([5., 2., 5., 0., 0.])
>>> a=np.array([1,1,4,5,5,7],float)
>>> np.unique(a)
array([1., 4., 5., 7.])
>>> a=np.array([[1,2],[3,4]],float)
>>> np.diagonal()
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    np.diagonal()
  File "<__array_function__ internals>", line 4, in diagonal
TypeError: _diagonal_dispatcher() missing 1 required positional argument: 'a'
>>> a.diagonal()
array([1., 4.])
>>> a=np.array([1,3,0],float)
>>> b=np.array([0,3,2],float)
>>> a>b
array([ True, False, False])
>>> a==b
array([False,  True, False])
>>> a<=b
array([False,  True,  True])
>>> a=a>b
>>> c
array([7., 8., 9.])
>>> a=np.array([1,3,0],float)
>>> a>2
array([False,  True, False])
>>> c=np.array([1,3,0],float)
>>> a>2
array([False,  True, False])
>>> c=np.array([True,False,False],bool)
>>> any(c)
True
>>> all(c)
False
>>> a=np.array([1,3,0],float)
>>> np.logical_and(a>0,a<3)
array([ True, False, False])
>>> b=np.array([True,False,True],bool)
>>> np.logical_not(b)
array([False,  True, False])
>>> c=np.array(False,True,False],bool)
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> c=np.array([False,True,False],bool)
>>> np.logical_or(b,c)
array([ True,  True,  True])
>>> a=np.array([1,3,0],float)
>>> np.where(a!=0,1/a,a)

Warning (from warnings module):
  File "<pyshell#199>", line 1
RuntimeWarning: divide by zero encountered in true_divide
array([1.        , 0.33333333, 0.        ])
>>> np.where(a>0,3,2)
array([3, 3, 2])
>>> a=np.array([[0,1],[3,0]],float)
>>> a.nonzero()
(array([0, 1], dtype=int64), array([1, 0], dtype=int64))
>>> a=np.array([1,np.NaN,np.Inf],float)
>>> a
array([ 1., nan, inf])
>>> np.isnan(a)
array([False,  True, False])
>>> np.isfinite(a)
array([ True, False, False])
>>> a=np.array([[6,4],[5,9],float)
	   
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> a=np.array([[6,4],[5,9]],float)
>>> a>=6
array([[ True, False],
       [False,  True]])
>>> a[a>=6]
array([6., 9.])
>>> a=np.array([6,4],[5,9]],float)
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> a=np.array([[6,4],[5,9]],float)
>>> sel=a(a>=6)
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    sel=a(a>=6)
TypeError: 'numpy.ndarray' object is not callable
>>> a=np.array([[6,4],[5,9]],float)
>>> sel=(a>=6)
>>> a[sel]
array([6., 9.])
>>> a[np.logical_and(a>5,a<9)]
array([6.])
>>> array([6.])
array([6.])
>>> a=np.array([2,4,6,8],float)
>>> b=np.array([0,0,1,3,2,1],int)
>>> a[b]
array([2., 2., 4., 8., 6., 4.])
>>> a=np.array([2,4,6,8],float)
>>> a[[0,0,1,3,2,1]]
array([2., 2., 4., 8., 6., 4.])
>>> a=np.array([[1,4],[9,16]],float)
>>> b=np.array([0,0,1,1,0],int)
>>> c=np.array([0,1,1,1,1],int)
>>> a[b,c]
array([ 1.,  4., 16., 16.,  4.])
>>> a=np.array([2,4,6,8],int)
>>> a.take(b)
array([2, 2, 4, 4, 2])
>>> a=np.array([[0,1],[2,3]],float)
>>> b=np.array([0,0,1],int)
>>> a.take(b,axis=0)
array([[0., 1.],
       [0., 1.],
       [2., 3.]])
>>> a.take(b,axis=1)
array([[0., 0., 1.],
       [2., 2., 3.]])
>>> a=np.array([0,1,2,3,4,5],float)
>>> a.put([0,3],5)
>>> a
array([5., 1., 2., 5., 4., 5.])
>>> a=np.array([1,2,3],float)
>>> b=np.array([0,1,1],float)
>>> np.dot(a,b)
5.0
>>> a=np.array([[0,1],[2,3]],float)
>>> b=np.array([2,3],float)
>>> c=np.array([[1,1],[4,0]],float)
>>> a
array([[0., 1.],
       [2., 3.]])
>>> np.dot(b,a)
array([ 6., 11.])
>>> np.dot(a,b)
array([ 3., 13.])
>>> np.dot(a,c)
array([[ 4.,  0.],
       [14.,  2.]])
>>> np.dot(a,c)
array([[ 4.,  0.],
       [14.,  2.]])
>>> np.dot(c,a)
array([[2., 4.],
       [0., 4.]])
>>> 