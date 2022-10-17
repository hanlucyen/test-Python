from decimal import *
import os
import math

for a in range(1,10):
            print(a,end=" ")
for x in range(1,10):
   print(x,end=" ")
def mysquare_root(a):
   epsilon=0.001 
while True:
   print(x)
y = (x + a / x) / 2
if abs(y-x)<epsilon:
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
#function prints the table, but the alignment is not good.
def list_func():
   for a in range(1, 10):
       print(float(a), " " * 20, f ("{mysquare_root(a)}"), " " * 20, f ("{square_root(a)}"), " " * 20, f ("{difference(a)}"))
list_func()

# by using the below functions("dec_1, dec_2") we are fixing the decimals after point to
#..........
'15'
numbers
#for uniform alignment.
# the 1 st
#function is
#for square_root which is built in function
# 2n d is
#for alignment of difference after built_in_
#function values.
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
       print(float(a), " " * 20, f ("{dec_1(a)}"), ' ' * 9, f ("{dec_2(a)}"), ' ' * 9, f ("{difference(a)}"))

print_it()
