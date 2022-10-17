#câu 1
#
import random
import math 
day = 365
sohocsinh = 23
n = 1000
#xác suất để có ít nhất 2 sinh viên cùng ngày sinh nhật trong 23 sinh viên
XS=1-((365/365)*(364/365)*(363/365)*(362/365)*(361/365)*(360/365)*(359/365)*(358/365)*(357/365)*(356/365)*(355/365)*(354/365)*(363/365)*(352/365)*(351/365)*(350/365)*(349/365)*(348/365)*(347/365)*(346/365)*(345/365)*(343/365)*(342/365))
print("xác suất để có ít nhất 2 sinh viên cùng ngày sinh nhật trong 23 sinh viên",XS)


def soNguoiTrung(my_list):
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) > 1: #dùng count để đếm số phần tử trùng nhau trong list
            return True
        elif i == (len(my_list) - 1):
            return False
        i += 1
def random_ngaysinh():
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
    
 


def solanlap(n):
    songuoi_trungsinhnhat = 0
    for i in range(n):
        if soNguoiTrung(random_ngaysinh()):
            songuoi_trungsinhnhat += 1
    print('Có {} sinh vien trung sinh nhật! '.format(songuoi_trungsinhnhat))
solanlap(n)
n=1000
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

#câu 2

"""
import numpy as np

def luytien(a):
    b=np.cumsum(a)
    return b

c=[4,6,22]
print(luytien(c))

"""
#C1
def accum(lis):
    total=0
    for x in lis:
        total+=x
        yield total#năng suất tổng
print(list(accum([2,4,3,21,9])))
#C2
import numpy as np
nhapMang=int(input("Độ dài  Mảng:"))

a=[]
for i in range(1,nhapMang+1):
    giatri=int(input("nhập giá trị của các phần tử trong mảng \n (!!!enter để nhập phần tử kế tiếp!!!): "))
    a.append(giatri)
    
def tongdon(a):
    d=np.cumsum(a)
    return d



print(tongdon(a))









#câu 3
f= open("words.txt")
lists = []
nhap_vao = [str(input("Nhập vào một từ tiếng Anh cần tìm trong file: "))]

for line in f:
    world = line.strip()
    lists.append(world)

def kiem_tra():
    # Chia file làm đôi
    ben_trai = lists[:500]
    ben_phai = lists[500:]
    if set(nhap_vao) & set(ben_trai):
        print("Từ này nằm ở bên trái và có trong file words.txt: {}".format(list(set(nhap_vao) & set(nhap_trai))))
        #dùng format để truyền giá trị vào {}
    elif set(nhap_vao) & set(ben_phai):
        print("Từ này nằm ở bên phải và có trong file words.txt: {}".format(list(set(nhap_vao) & set(nhap_phai))))

    else:
        print("Từ này không nằm trong file words.txt")
kiem_tra()




