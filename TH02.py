"""
#câu 1
#if
import math
x=int(input())
if x==100:
    print("gia tri cua x la 100")
if x!=100:
    print("gia tri cua x khac 100")
#if...else
import math
x=int(input())
if x==100:
    print("gia tri cua x la 100")
else:
    print("gia tri cua x khac 100")
#câu 2
import math
a=int(input())
b=int(input())
if a!=0:
    nghiem=-b/a
    print("Phuong trinh co nghiem duy nhat: ",nghiem)
if a==0:
    if b==0:
        nghiem1=-b
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo so nghiem")

#câu 3
import math
from datetime import datetime
month=int(input())
year=int(input())
print("thang ",month)
print("nam ",year)
if (month==1) or (month==3) or (month==5) or (month==7) or (month==8) or (month==10) or (month==12):
    print( "Thang co 31 ngay")
if (month==4) or (month==4) or (month==6) or (month==9) or (month==11):
    print("Thang co 30 ngay")
if month==2:
    if (year%400==0) or ((year%4==0)and (year%100!=0)):
        print("Nam nhuan thang 2 co 29 ngay")
    else:
        print("Nam khong nhuan thang 2 co 28 ngay")

#câu 4
import math
a=int(input())
b=int(input())
c=int(input())
if (a+b>c):
    print( "TH1 khong co tam giac")
if (b+c>a):
    print( "TH2 khong co tam giac")
if (a+c>b):
    print( "TH3 khong co tam giac")
else:
    print("co tam giac")
#vì cho cặp số nào cũng là các trường hợp không có tam giác .không thể xét sau else (em chưa biết sửa)
#vì phía trên khá chung chung nên làm lại
  
"""  
import math
a=int(input())
b=int(input())
c=int(input())
if (a+b>c):
    print( "TH1 khong co tam giac")
if (b+c>a):
    print( "TH2 khong co tam giac")
if (a+c>b):
    print( "TH3 khong co tam giac")
if (a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b):
    print("tam giac vuong")
if (a==b==c):
    print("tam giac deu")
if (a*a>b*b+c*c) or (b*b>a*a+c*c) or (c*c>a*a+b*b):
    print("tam giac tu")
else:
    print("tam giac nhon")



