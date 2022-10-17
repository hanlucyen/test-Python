import math
print(" ")
epsilon=0.001
def mysqrt(x,a):
    while True:
        
        print("nhap gia tri phong doan gia tri ban dau : ")
        x=float(input())
        y=(x+a/x)/2
        if abs(y-x)<epsilon:
           break
        x=y

print(mysqrt())
for a in range(1,10):
            print(a,end=" ")

mysqrt(1,1),mysqrt(2,2),mysqrt(3,3),mysqrt(4,4),mysqrt(5,5),mysqrt(6,6),mysqrt(7,7),mysqrt(8,8),mysqrt(9,9)
def module_math():
  print(" Su dung ham sqrt trong module math de tinh lai")
  for a in range(1,10):
    b=math.sqrt(a)
    print(a," -",b)
module_math()


import math
import pandas as pd
import numpy as py
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
def deviated():
  diff=fuction_math()-mysqrt(x,a)
  return diff

deviated()
print("sai lech giua hai thuat toan")
print('a', ' ' * 1, 'mysqrt(a)', ' ' * 3, 'math.sqrt(a)', ' diff')
print('-', ' ' * 1, '-' * 9, ' ' * 3, '-' * 12, ' ' + '-' * 4)
