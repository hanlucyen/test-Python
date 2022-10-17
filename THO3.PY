"""
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

#\n
import math
tong=0
n=1
i=1
print("nhap so n : ")
n=int(input())
i=i+1
while True:
    if i%4==0 and i%5!=0:
        tong=tong+i
    if i==n:
        print(tong)
        break
    if i!=n:
        i=int(input())
"""
#\n
i=0
a=0
tong=[]
n=int(input(' nhap n '))
while True:
    if n>=12:
        if i<=n and i%4==0 and i%5!=0:
            tong.append(i+a)
        if i>n:
            print('tong: ',sum(tong))
            break
        i=i+1
    if n<12:
        n=int(input('nhap lai:' ))
    if n<=0:
        print('nhap lai n>=12')
        n=int(input('please n: '))
