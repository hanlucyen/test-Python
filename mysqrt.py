import math
import sys
import os


print("nhap vao gia tri ban dau a la : ")
a=int(input())


def mysqrt():
    while True:
        for a in range(1,10):
            print(a,end=" ")
        print("nhap gia tri phong doan gia tri ban dau : ")
        x=float(input())
        y=(x+a/x)/2
        if abs(y-x) <.001:
            break
        x=y

print(mysqrt())

b=math.sqrt(a)
print(" sqrt su dung module math : ",b)
        
for a in range(1,10):
    print(a,end=" ")
import pandas as pd
s={'a':pd.Series([1,2,3,4,5,6,7,8,9]),'mysqrt(a)': pd.Series([a]),
   'a':pd.Series([1,2,3,4,5,6,7,8,9]),'math.sqrt(a)':pd.Series([a])}
#tại DataFrame từ dict
df=pd.DateFrame(s)
print(df)
import math
import pandas as pd
a=int(input())
x=int(input())
y=(x+a/x)/2
print(y)
def mysqrt():
    while True:
        print("\n","gia tri dau")
        a=int(input())
        print("so phong doan ")
        x=int(input())
        y = (x + a/x)/2
        if abs(y-x) <.001:
           break
        x = y

print(mysqrt())

c=math.sqrt(a)
print("math.sqrt la: ",c)
diff=int(x-c)
print("sai lech",diff)
for a in range(1,10):
    print(a,end=" " )
f=list(1,1.41421356237,1.73205080757,2,2.2360679775,2.44948974278,2.64575131106,2.82842712475,3)
e=sqrt(1),sqrt(2),sqrt(3),sqrt(4),sqrt(5),sqrt(6),sqrt(7),sqrt(8),sqrt(9)
df=pd.DtaFrame[[f],[e],[f-e]],index=[a],colums=list('a','mysqrt(a)','math.sqrt(a)','diff')\n list('- -------- ---------- ---')
import math
epsilon = 0.00000000001

def mysqrt(a):
   x = a / 2
while True:
   y = (x + a / x) / 2
if abs(y - x) < epsilon:
   return y
break
x = y

def right_digit(n):
   ''
'Takes a floating point number and returns its right
most digit in 'str'
format ''
'
trunc = f '{n:.11f}'
dig = trunc[len(trunc) - 1]
return dig

def test_square_root(n):
   print('a', ' ' * 1, 'mysqrt(a)', ' ' * 3, 'math.sqrt(a)', ' diff')
print('-', ' ' * 1, '-' * 9, ' ' * 3, '-' * 12, ' ' + '-' * 4)

for i in range(9):
   x = i + 1

print(f '{x:0.1f}', end = ' ')

if mysqrt(x) - int(mysqrt(x)) < 0.001:
   y = 1
elif right_digit(mysqrt(x)) == '0':
   y = 10
else :
   y = 11

print(f '{mysqrt(x):<13.{y}f}', end = ' ')
print(f '{mysqrt(x):<13.{y}f}', end = ' ')

diff = math.sqrt(x) - mysqrt(x)
print(f '{diff:.12g}')

test_square_root(9)
The resulting table looks something like this:

a mysqrt(a) math.sqrt(a) diff -
   -- -- -- -- - -- -- -- -- -- -- -- --
1.0 1.0 1.0 0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0
4.0 2.0 2.0 0
5.0 2.2360679775 2.2360679775 0
6.0 2.44948974278 2.44948974278 0
7.0 2.64575131106 2.64575131106 0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0 3.0 0
You can use the tab \t in the print statement:

print("\t", a, "\t", y, "\t", square_method, "\t"
   "diff:", diff, )
here is my code which looks good:

from decimal
import *
import math

def mysquare_root(a):
   x = 1
while True:
   #print(x)
y = (x + a / x) / 2
if x == y:
   break
x = y
return (x)

def square_root(a):
   x = math.sqrt(a)
return x
def difference(a):
   d = square_root(a) - mysquare_root(a)
return d

# the below
function prints the table, but the alignment is not good.
def list_func():
   for a in range(1, 10):
   print(float(a), " " * 20, f "{mysquare_root(a)}", " " * 20, f "{square_root(a)}", " " * 20, f "{difference(a)}")
list_func()

# by using the below functions("dec_1, dec_2") we are fixing the decimals after point to
#..........
'15'
numbers
for uniform alignment.
# the 1 st
function is
for square_root which is built in function
# 2n d is
for alignment of difference after built_in_
function values.
def dec_1(a):
   d = Decimal(mysquare_root(a))
#print(d)
d1 = round(d, 15)
#print(d1)
#print(d1)
return Decimal(d1)

def dec_2(a):
   d = Decimal(square_root(a))
#print(d)
d1 = round(d, 15)
#print(d1)
return Decimal(d1)

def print_it():
   for a in range(1, 10):
   print(float(a), " " * 20, f "{dec_1(a)}", ' ' * 9, f "{dec_2(a)}", ' ' * 9, f "{difference(a)}")

print_it()
def square_root(a):
    x = math.sqrt(a)
    return x
def difference(a):
    d = square_root(a) - mysqrt()
    return d
def list_func():
    for a in range(1, 10):
        print(float(a), " " * 20, f ("{mysqrt(a)}"), " " * 20,f ("{square_root(a)}"), " " * 20, f ("{difference(a)}"))
list_func()


def dec_1(a):
    d = Decimal(mysqrt())
#print(d)
    d1 = round(d, 15)
#print(d1)
#print(d1)
    return Decimal(d1)

def dec_2(a):
   d = Decimal(square_root(a))
#print(d)
   d1 = round(d, 15)
#print(d1)
   return Decimal(d1)

def print_it():
    for a in range(1, 10):
        print(float(a), " " * 20, f ("{dec_1(a)}"), ' ' * 9, f ("{dec_2(a)}"), ' ' * 9, f ("{difference(a)}"))

print_it()
import math
import pandas as pd
import numpy as np
print("ap dung thuat toan newton de tinh ")
epsilon=0.001
def mysqrt(x,a):
  while True:
    print(x)
    y=(x+a/x)/2
    if abs(y-x)<epsilon:
      break
    x=y
mysqrt(1,1),mysqrt(2,2),mysqrt(3,3),mysqrt(4,4),mysqrt(5,5),mysqrt(6,6),mysqrt(7,7),mysqrt(8,8),mysqrt(9,9)
def fuction_math():
  print("su dung ham sqrt trong module math")
  for a in range(1,10):
    b=math.sqrt(a)
    print(a," -",b)
fuction_math()

print("sai lech giua hai thuat toan")
print('a', ' ' * 1, 'mysqrt(a)', ' ' * 3, 'math.sqrt(a)', ' diff')
print('-', ' ' * 1, '-' * 9, ' ' * 3, '-' * 12, ' ' + '-' * 4)
print(1,' ',mysqrt(1,1),2,' ',mysqrt(2,2),3,' ',mysqrt(3,3),4,' ',mysqrt(4,4),5,' ',mysqrt(5,5),6,' ',mysqrt(6,6),7,' ',mysqrt(7,7),8,' ',mysqrt(8,8),9,' ',mysqrt(9,9))
