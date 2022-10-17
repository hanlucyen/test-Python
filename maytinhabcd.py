print("Máy tính")
import numpy
mylistnum=[]
print('Nhập "stop" khi muốn dừng')
while True:
    val=input('Nhập một số: ')
    if val=='stop':
            print('Kết thúc')
            break
    mylistnum.append(int(val))
print(mylistnum)
tong=0
for i in mylistnum:
    tong+=i
print(tong)
hieu=0
for i in mylistnum:
    tong-=i
print(hieu)
tich=0
for i in mylistnum:
    tong*=i
print(tich)
thuong=0
for i in mylistnum:
    tong%=i
print(thuong)
