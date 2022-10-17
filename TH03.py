#bài 1
from math import *
def eval_loop(eval):
    return eval
while True:
    import math
    print("nhap tu ban phim")
    x = eval('input("Enter a letter: ")')
    if x!='done':
        print(eval(x))
    if x=='done':
       break
print('Done!')
print(eval_loop(eval))

#bài 2
import math
tong=0
n=1
i=1
print("nhap so n : ")
n=int(input())
while i<=n:
    tong+=i
    i+=1
print("tong cua n so la : ",tong)

#bài 3
#a
import math
tong=0
n=1
i=1
print("nhap so n : ")
n=int(input())
while i<=n:
    tong+=i
    i+=1
print("tong cua n so la : ",tong)
if tong%4==0 and tong%5!=0:
    print("nhan ")
else:
    print("loai")
#b
import math
tong=0
n=1
i=1
print("nhap so n : ")
n=int(input())

while True:
    if n>=12:
        while i<=n:
            tong+=i
            i+=1
            print("tong cua n so la : ",tong)
        if tong%4==0 and tong%5!=0:
            print("nhan ")
        else:
            print("loai")
        break
    if n<=12:
        n=int(input())
    
#bài 4
from math import *
n=int(input())
if 0<=n<=50:
    print("nhap n tu ban phim: ",n)
    if n>=2 or n%n==0 or n%1==n:
        print("la so nguyen to ")
    else:
        print("khong phai so nguyen to")
i=list(range(2,50))
print(i)
if min(i)%min(i)==0 or min(i)%min(1)==i:
    print("so nguyen to nho nhat",min(i))
else:
    print("so nguyen to")




