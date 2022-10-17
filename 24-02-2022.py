Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=np.array([1,4,0],float)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=np.array([1,4,0],float)
NameError: name 'np' is not defined
>>> import numpy as py
>>> a=np.array([1,4,0],float)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a=np.array([1,4,0],float)
NameError: name 'np' is not defined
>>> import numpy as np
>>> a=np.array([1,4,0],float)
>>> b=np.array([2,2,1],float)
>>> np.outer(a,b)
array([[2., 2., 1.],
       [8., 8., 4.],
       [0., 0., 0.]])
>>> np.inner(a,b)
10.0
>>> np.cross(a,b)
array([ 4., -1., -6.])
>>> a=np.array([[4,2,0],[9,3,7],[1,2,1]],float)
>>> a
array([[4., 2., 0.],
       [9., 3., 7.],
       [1., 2., 1.]])
>>> np.linalg.det(a)
-48.00000000000003
>>> vals,vecs=np.linalg.eig(a)
>>> vals
array([ 8.85591316,  1.9391628 , -2.79507597])
>>> vecs
array([[-0.3663565 , -0.54736745,  0.25928158],
       [-0.88949768,  0.5640176 , -0.88091903],
       [-0.27308752,  0.61828231,  0.39592263]])
>>> b=np.linalg.inv(a)
>>> b
array([[ 0.22916667,  0.04166667, -0.29166667],
       [ 0.04166667, -0.08333333,  0.58333333],
       [-0.3125    ,  0.125     ,  0.125     ]])
>>> np.dot(a,b)
array([[ 1.00000000e+00,  0.00000000e+00, -2.22044605e-16],
       [ 0.00000000e+00,  1.00000000e+00, -2.77555756e-17],
       [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])
>>> a=np.array([[1,3,4],[5,2,3]],float)
>>> U,s,Vh=np.linalg.svd(a)
>>> U
array([[ 0.6113829 , -0.79133492],
       [ 0.79133492,  0.6113829 ]])
>>> s
array([7.46791327, 2.86884495])
>>> Vh
array([[ 0.61169129,  0.45753324,  0.64536587],
       [ 0.78971838, -0.40129005, -0.46401635],
       [-0.046676  , -0.79349205,  0.60678804]])
>>> np.poly([-1,1,1,10])
array([  1., -11.,   9.,  11., -10.])
>>> np.roots([1,4,-2,3])
array([-4.5797401 +0.j        ,  0.28987005+0.75566815j,
        0.28987005-0.75566815j])
>>> np.polyint([1,1,1,1])
array([0.25      , 0.33333333, 0.5       , 1.        , 0.        ])
>>> np.polyder([1/4.,1./3.,1./2.,1.,0.])
array([1., 1., 1., 1.])
>>> np.polyval([1,-2,0,2],4)
34
>>> x=[1,2,3,4,5,6,7,8]
>>> y=[0,2,1,3,7,10,11,19]
>>> np.polyfit(x,y,2)
array([ 0.375     , -0.88690476,  1.05357143])
>>> a=np.array([1,4,3,8,9,2,3],float)
>>> np.median(a)
3.0
>>> a=np.array([[1,2,1,3],[5,3,1,8]],float)
>>> c=np.corrcoef(a)
>>> c
array([[1.        , 0.72870505],
       [0.72870505, 1.        ]])
>>> np.cov(a)
array([[0.91666667, 2.08333333],
       [2.08333333, 8.91666667]])
>>> np.random.seed(293423)
>>> np.random.rand(5)
array([0.33677247, 0.52693437, 0.79529578, 0.78867702, 0.02147624])
>>> np.random.rand(2,3)
array([[0.84612516, 0.0704939 , 0.1526965 ],
       [0.77831701, 0.80821151, 0.82198398]])
>>> np.array.rand(6).reshape((2,3))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    np.array.rand(6).reshape((2,3))
AttributeError: 'builtin_function_or_method' object has no attribute 'rand'
>>> np.random.rand(6).reshape((2,3))
array([[0.90239653, 0.8385685 , 0.02638565],
       [0.33681448, 0.46480928, 0.61686496]])
>>> np.random.random()
0.43767262538051455
>>> np.random.randint(5,10)
5
>>> np.ranom.poisson(6.0)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    np.ranom.poisson(6.0)
  File "C:\Users\ASUS\anaconda3\lib\site-packages\numpy\__init__.py", line 303, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'ranom'
>>> np.random.poisson(6.0)
4
>>> np.random.normal(1.5,4.0)
-1.5224080889736675
>>> np.random.normal()
0.957100788846741
>>> np.random.normal(size=5)
array([-1.01092541,  0.58092445,  1.122653  , -0.1252049 ,  0.57716007])
>>> l=range(10)
>>> l
range(0, 10)
>>> np.random.shuffle(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    np.random.shuffle(l)
  File "mtrand.pyx", line 4485, in numpy.random.mtrand.RandomState.shuffle
  File "mtrand.pyx", line 4488, in numpy.random.mtrand.RandomState.shuffle
TypeError: 'range' object does not support item assignment
>>> np.random.shuffle(l)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    np.random.shuffle(l)
  File "mtrand.pyx", line 4485, in numpy.random.mtrand.RandomState.shuffle
  File "mtrand.pyx", line 4488, in numpy.random.mtrand.RandomState.shuffle
TypeError: 'range' object does not support item assignment
>>> l=range(10)
>>> l
range(0, 10)
>>> np.random.shuffle(l)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    np.random.shuffle(l)
  File "mtrand.pyx", line 4485, in numpy.random.mtrand.RandomState.shuffle
  File "mtrand.pyx", line 4488, in numpy.random.mtrand.RandomState.shuffle
TypeError: 'range' object does not support item assignment
>>> import scipy
>>> help(scipy)

>>> import scipy
>>> import scipy.interpolate
>>> 