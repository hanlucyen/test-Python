"""
import random
import os
n=1000

while n>1:
    
    def ran_dom_ngau_nhien(list):
    
        val1 = random.randint(1, 365)
        print(val1)
 
        val2 = random.randint(1, 365)
        print(val2)
        val3 = random.randint(1, 365)
        print(val3)
        val4 = random.randint(1, 365)
        print(val4)


     
        val5 = random.randint(1, 365)
        print(val5)
     
        val6 = random.randint(1, 365)
        print(val6)
     
        val7 = random.randint(1, 365)
        print(val7)
     
        val8 = random.randint(1, 365)
        print(val8)


     
        val9 = random.randint(1, 365)
        print(val9)
     
        val10 = random.randint(1, 365)
        print(val10)
     
        val11 = random.randint(1, 365)
        print(val11)
     
        val12 = random.randint(1, 365)
        print(val12)


     
        val13 = random.randint(1, 365)
        print(val13)
     
        val14 = random.randint(1, 365)
        print(val14)
     
        val15 = random.randint(1, 365)
        print(val15)

        val16 = random.randint(1, 365)
        print(val16)
        val17 = random.randint(1, 365)
        print(val17)



     
        val18 = random.randint(1, 365)
        print(val18)
     
        val19 = random.randint(1, 365)
        print(val19)
     
        val20 = random.randint(1, 365)
        print(val20)
     

     
        val21 = random.randint(1, 365)
        print(val21)
     
        val22 = random.randint(1, 365)
        print(val22)
     
        val23 = random.randint(1, 365)
        print(val23)
     
        
        list=(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21,val22,val23)
        return list

       

        
    co_py=ran_dom_ngau_nhien(list)
    print(co_py)
    tr_ung=list(dict.fromkeys(co_py))
    print(tr_ung)


    i=0
    dem=0
    x=0
    if len(co_py)!=len(set(tr_ung)):
        x=1
        print('x:',x)
    else:
        i=i

    def ket_qua():
        so_lan_chay= 0
        for i in range(1,100):
            #Kiểm tra xem các phần tử của 2 list có trùng nhau không
            if set(co_py) & set(tr_ung):
                print("Các sinh viên có cùng ngày sinh là các ngày: {} ".format(list(set(co_py) & set(tr_ung))))
                print("Số lần phát hiện ra 2 sinh viên có cùng ngày sinh là: {} ".format(len( set(co_py) & set(tr_ung))))
                so_lan_chay += 1
                print("Số lần thực hiện chương trình là: {}".format(so_lan_chay))
                break
            else:
                print("Không có sinh viên nào có cùng ngày sinh")
                so_lan_chay+=1
                print("Số lần thực hiện chương trình là: {}".format(so_lan_chay))
    ket_qua()
"""
"""
    i=i+x
    dem=i+1
    print("ra chua",dem)


      


while x==1:
            i=i+x
            dem=i+1
            print("tổng số lần lặp",dem)
            if dem
    

    def check_duplicate_list():
        if len(co_py)!=len(set(tr_ung)):
            return "Tồn tại phần tử trùng lặp trong list"
        else:
            return "Không có phần tử trùng lặp trong list"  

    print(check_duplicate_list())
    n -=1
    print("lần thứ: ",n)
    
  """
"""
import random
from math import log10, factorial
day = 365
n = 23
print("Tổng số sinh viên là: {} sinh viên".format(int(n)))
print("Số ngày sinh đã bỏ qua ngày 29/2 là: {} ngày ".format(int(day)))

#Tính xác suất của 2 trong 23 sinh viên có cùng ngày sinh
tu_so = factorial(day)
mau_so = (day**n)*factorial(day - n)
ket_qua = log10(tu_so) - log10(mau_so)
print("Xác xuất để có hai người sinh cùng ngày là: {}".format(1.0-(10**ket_qua)))

#Chọn ngẫu nhiên 23 ngày sinh từ 1 đến 365 của lần 1
birthday_1 = []
for i in range(1, 23 + 1):
    day_1 = random.randint(1, 365)
    birthday_1.append(day_1)

#Chọn ngẫu nhiên 23 ngày sinh từ 1 đến 365 của lần 2
birthday_2 = []
for i in range(1,23+1):
    day_2 = random.randint(1, 365)
    birthday_2.append(day_2)

#Tính số lần chạy chương trình và tìm kiếm các ngày sinh trùng nhau
def ket_qua():
    so_lan_chay= 0
    for i in range(1,100):
        #Kiểm tra xem các phần tử của 2 list có trùng nhau không
        if set(birthday_1) & set(birthday_2):
            print("Các sinh viên có cùng ngày sinh là các ngày: {} ".format(list(set(birthday_1) & set(birthday_2))))
            print("Số lần phát hiện ra 2 sinh viên có cùng ngày sinh là: {} ".format(len( set(birthday_1) & set(birthday_2))))
            so_lan_chay += 1
            print("Số lần thực hiện chương trình là: {}".format(so_lan_chay))
            break
        else:
            print("Không có sinh viên nào có cùng ngày sinh")
            so_lan_chay+=1
            print("Số lần thực hiện chương trình là: {}".format(so_lan_chay))
ket_qua()

print("-----------")

import random
import math 
day = 365
n = 23
#xác suất để có ít nhất 2 sinh viên cùng ngày sinh nhật trong 23 sinh viên
XS=1-((365/365)*(364/365)*(363/365)*(362/365)*(361/365)*(360/365)*(359/365)*(358/365)*(357/365)*(356/365)*(355/365)*(354/365)*(363/365)*(352/365)*(351/365)*(350/365)*(349/365)*(348/365)*(347/365)*(346/365)*(345/365)*(343/365)*(342/365))
print("xác suất để có ít nhất 2 sinh viên cùng ngày sinh nhật trong 23 sinh viên",XS)
#chọn ngẫu nhiên 
birthday1 = []
for i in range(1, 23 + 1):
    co_py = random.randint(1, 365)
    birthday1.append(co_py)

birthday2 = []
for i in range(1,23+1):
    day_2 = random.randint(1, 365)
    birthday2.append(day_2)
def ket_qua():
    chayLan= 0
    for i in range(1,1000):
        #Kiểm tra sự trùng lặp các phần tử trong 2 list 
        if set(birthday1) & set(birthday2):
            print("Số sinh viên có cùng ngày sinh là các ngày: {} ".format(list(set(birthday1)& set(birthday2))))
            print("Số lần phát hiện ra 2 sinh viên có cùng ngày sinh là: {} ".format(len( set(birthday1) & set(birthday2))))
            chayLan += 1
            print("Số lần chạy chương trình là: {}".format(chayLan))
            break
        else:
            print("Không có sinh viên cùng ngày sinh")
            chayLan +=1
            print("Số lần chạy chương trình là: {}".format(chayLan))
ket_qua()







"""
import math
import random

n=10
while n>1:
      
    def ran_dom_ngau_nhien(list):
        val1 = random.randint(1, 365)
        val2 = random.randint(1, 365)
        val3 = random.randint(1, 365)
        val4 = random.randint(1, 365)
        val5 = random.randint(1, 365)
        val6 = random.randint(1, 365)
        val7 = random.randint(1, 365)
        val8 = random.randint(1, 365)
        val9 = random.randint(1, 365)
        val10 = random.randint(1, 365)
        val11 = random.randint(1, 365)
        val12 = random.randint(1, 365)
        val13 = random.randint(1, 365)
        val14 = random.randint(1, 365)
        val15 = random.randint(1, 365)
        val16 = random.randint(1, 365)
        val17 = random.randint(1, 365)
        val18 = random.randint(1, 365)
        val19 = random.randint(1, 365)
        val20 = random.randint(1, 365)
        val21 = random.randint(1, 365)
        val22 = random.randint(1, 365)
        val23 = random.randint(1, 365)


        list=(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21,val22,val23)
        return list

       

        
    co_py=ran_dom_ngau_nhien(list)
    print(co_py)
    tr_ung=list(dict.fromkeys(co_py))
    print(tr_ung)


    n -=1
    print("lần thứ: ",n)
    def check_duplicate_list():
            if len(co_py)!=len(set(tr_ung)):
                return "Tồn tại phần tử trùng lặp trong list"
            else:
                return "Không có phần tử trùng lặp trong list"  

    print(check_duplicate_list())
      

         

a=23
n=1000
tongtrung=0
for i for range(1000):
    print("số lần thực hiện phép tính",i)
ii=23
iii="số lần phát hiện ra 2 sv trùng ngày sinh"
"""

import math
import random
n=10
while n>1:
    
    def ran_dom_ngau_nhien(list):
    
        val1 = random.randint(1, 365)
        print(val1)
 
        val2 = random.randint(1, 365)
        print(val2)
        val3 = random.randint(1, 365)
        print(val3)
        val4 = random.randint(1, 365)
        print(val4)


     
        val5 = random.randint(1, 365)
        print(val5)
     
        val6 = random.randint(1, 365)
        print(val6)
     
        val7 = random.randint(1, 365)
        print(val7)
     
        val8 = random.randint(1, 365)
        print(val8)


     
        val9 = random.randint(1, 365)
        print(val9)
     
        val10 = random.randint(1, 365)
        print(val10)
     
        val11 = random.randint(1, 365)
        print(val11)
     
        val12 = random.randint(1, 365)
        print(val12)


     
        val13 = random.randint(1, 365)
        print(val13)
     
        val14 = random.randint(1, 365)
        print(val14)
     
        val15 = random.randint(1, 365)
        print(val15)

        val16 = random.randint(1, 365)
        print(val16)
        val17 = random.randint(1, 365)
        print(val17)



     
        val18 = random.randint(1, 365)
        print(val18)
     
        val19 = random.randint(1, 365)
        print(val19)
     
        val20 = random.randint(1, 365)
        print(val20)
     

     
        val21 = random.randint(1, 365)
        print(val21)
     
        val22 = random.randint(1, 365)
        print(val22)
     
        val23 = random.randint(1, 365)
        print(val23)
     
        
        list=(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21,val22,val23)
        return list

       

        
    co_py=ran_dom_ngau_nhien(list)
    print(co_py)
    tr_ung=list(dict.fromkeys(co_py))
    print(tr_ung)
    


    











        


    def check_duplicate_list():
        if len(co_py)!=len(set(tr_ung)):
            return "Tồn tại phần tử trùng lặp trong list"
        else:
            return "Không có phần tử trùng lặp trong list"  

    print(check_duplicate_list())
    n -=1
    print("lần thứ: ",n)
    
    if len(co_py)!=len(set(tr_ung)):
        print(int(1))
    else:
        print(int(0) 
    







