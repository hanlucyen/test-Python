
print('Nghich ly Ngay Sinh Nhat')
import random
sohocsinh = 23
n = 1000
def nguoi_trung(my_list):
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) > 1:
            return True
        elif i == (len(my_list) - 1):
            return False
        i += 1
def ngaysinh_ngaunhien():
    while n>1:
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
    
   


def so_lieu(n):
    songuoi_trunglap = 0
    for i in range(n):
        if nguoi_trung(ngaysinh_ngaunhien()):
            songuoi_trunglap += 1
    print('Tong so lan thuc hien phep tinh: {} lan'.format(n))
    print('Tong so sinh vien: {}'.format(sohocsinh))
    print('Co  {} sinh vien co cung ngay sinh. '.format(songuoi_trunglap))
so_lieu(n)
print('{:*>30}'.format(''))

"""
import random
sohocsinh=23
n=1000
def trung(my_list):
    i=0
    while i< len(my_list):
        if my_list.count(my_list[i])>1:
            return True
        if i==(len(my_list)-1):
            return False
        i +=1
def ngaysinhngaunhien(list):
    while 1000>1:
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
        
print("list: ",(ngaysinhngaunhien(list)))

co_py=ngaysinhngaunhien(list)
print(co_py)
tr_ung=list(dict.fromkeys(co_py))
print(tr_ung)
def ket_qua(n):
    solanchay=0
    for i in range(n):
        if trung(ngaysinhngaunhien()):
            solanchay +=1
            print(solanchay)
print(ket_qua(n))
      
        if len(co_py)!=len(tr_ung):
            
            print("trùng")
        else:
            print("không Trùng")


       
        

        
def so_lieu(n):
    songuoitrung=0
    for i range(n):
        if trung(ngaysinhngaunhien)):
            songuoitrung +=1
    print("khi",songuoitrung)
"""      
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
