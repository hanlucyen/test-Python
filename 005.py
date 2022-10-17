
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
    return [random.randint(1, 365) for hocsinh in range(sohocsinh)]
   


def so_lieu(n):
    songuoi_trunglap = 0
    for i in range(n):
        if nguoi_trung(ngaysinh_ngaunhien()):
            songuoi_trunglap += 1
    print('Tong so lan thuc hien phep tinh: {} lan'.format(n))
    print('Tong so sinh vien: {}'.format(sohocsinh))
    print("Số lần phát hiện ra 2 sinh viên có cùng ngày sinh là: {} ".format(ngaysinh_ngaunhien))
    print('Co  {} sinh vien co cung ngay sinh. '.format(songuoi_trunglap))
so_lieu(n)
print('{:*>30}'.format(''))



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
    for i in range(1,10):
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
