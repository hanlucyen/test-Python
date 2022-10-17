"""tang="s0"
def thangmay(dieu_khien):
    global tang
    if tang=="s0":
        if dieu_khien==0:
            print("tím")
            tang="s0"
        elif dieu_khien==1:
            print("hồng")
            tang="s1"
    elif tang=="s1":
        if dieu_khien==0:
            print("hồng")
            tang="s1"
        elif dieu_khien==1:
            print("tím")
            tang="s0"
tap_dieukhien=[1,0,1,0,1,0,0]
for i in tap_dieukhien:

    thangmay(i)



"""



import os
import math
x="nguoigia"
y="treem"
w="nguoibithuongochan"
z="nguoibinhthuong"
print("nguoigia,treem,nguoibithuongochan,nguoibinhthuong")
print("nhập người muốn đi thang máy: ")
n=input()
if n==x or n==y or n==w:
    print("được đi thang máy")
    tang="s0"
    def thangmay(dieu_khien):
        global tang
        if tang=="s0":
            if dieu_khien==0:
                print("đèn chuyển tím")
                tang="s0"
            elif dieu_khien==1:
                print("đèn chuyển hồng")
                tang="s1"
        elif tang=="s1":
            if dieu_khien==0:
                print("đèn chuyển hồng")
                tang="s1"
            elif dieu_khien==1:
                print("đèn chuyển tím")
                tang="s0"
    print("nhập tầng muốn đi: 0 là tầng triệt, 1 là tầng 1 ")
    k=int(input())
    thangmay(k)
else:
    print("không thuộc đối tượng ưu tiên đi thang máy \nVui lòng đi thang bộ")
