"""
 392 ,Lê Văn Lương ,ấp 3, xã Phước Kiển ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 D08-05  ,khu căn hộ New Sài Gòn, ấp 5 ,xã Phước Kiển ,huyện Nhà Bè
 17 ,ấp 2 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 369 ,Đào Sư Tích ,ấp 4 ,xã Phước Lộc ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 456/55 ,Huỳnh Tấn Phát ,khu phố 7 ,Thị trấn Nhà Bè  ,huyện Nhà Bè
 A11-08 ,khu căn hộ New Sài Gòn ,ấp 5 ,xã Phước Kiển ,huyện Nhà Bè 
 485 ,Huỳnh Tấn Phát ,khu phố 7 ,Thị trấn Nhà Bè ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 51/1A ,Huỳnh Tấn Phát khu phố 6 ,thị trấn Nhà Bè ,huyện Nhà Bè
 519/9 ,Huỳnh Tấn Phát khu phố 7 ,Thị trấn Nhà Bè ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 342/108 ,Huỳnh Tấn Phát khu phố 6 thị trấn Nhà Bè huyện Nhà Bè
 B19-03 ,khu căn hộ  New  Sài Gòn ,ấp 5 ,xã Phước Kiển ,huyện Nhà Bè
 24/2B ,Khu phố 4 thị trấn Nhà Bè huyện Nhà Bè thành phố Hồ Chí Minh
 18.6 ,lô D  chung cư P  ,ấp 3 ,xã Phú Xuân ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 trường trung học phổ thông Long Thới  280 Nguyễn Văn Tạo   ,ấp 2 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 92A  ,ấp 3 ,xã Long Thới huyện Nhà Bè ,thành phố Hồ Chí Minh
 161 ,Lê Văn Lương ,ấp 5 xã Phước Kiển huyện Nhà Bè ,thành phố Hồ Chí Minh
 34/7 ,khu phố 4 ,thị trấn Nhà Bè huyện Nhà Bè ,thành phố Hồ Chí Minh
 64/6/35/2A ,Đào Tông Nguyên ,ấp 4 ,xã Phú Xuân ,huyện Nhà Bè thành ,phố Hồ Chí Minh
 71/27 ,Nguyễn Văn Tạo ,Ấp 1 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 133 ,Ấp 1 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 111/4A ,Lê Văn Lương ,ấp 3 ,xã Phước Kiển ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 12 ,lô A Nguyễn Văn Tạo Ấp 1 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh 
 4/5 ,khu phố 5 ,thị trấn Nhà Bè ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 125 ,ấp 3 ,xã Long Thới huyện Nhà Bè ,thành phố Hồ Chí Minh
 745 ,Nguyễn Văn Tạo ,Ấp 1 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 142 ,Huỳnh Tấn Phát ,thị trấn Nhà Bè ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 318 ,Nguyễn Văn Tạo ,ấp 2,0, xã Long Thới huyện Nhà Bè ,thành phố Hồ Chí Minh
 9A ,ấp 5   ,Xã Phước Kiển ,huyện Nhà Bè ,thành phố Hồ Chí Minh
 01 ấp 3 xã Phước Kiển huyện Nhà Bè ,thành phố Hồ Chí Minh
 A12-01  ,khu căn hộ New  Sài Gòn F5 ,xã Phước Kiển ,huyện Nhà Bè 
"""
import re
A1='392 , đường Lê Văn Lương ,ấp 3, xã Phước Kiển ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A2='D08-05  ,khu căn hộ New Sài Gòn, ấp 5 ,xã Phước Kiển ,huyện Nhà Bè'

A3='17 ,ấp 2 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A4='369 ,đường Đào Sư Tích ,ấp 4 ,xã Phước Lộc ,huyện Nhà Bè ,thành phố Hồ Chí Minh'
 
A5='456/55 ,đường Huỳnh Tấn Phát ,khu phố 7 ,thị trấn Nhà Bè  ,huyện Nhà Bè'
 
A6='A11-08 ,khu căn hộ New Sài Gòn ,ấp 5 ,xã Phước Kiển ,huyện Nhà Bè '
 
A7='485 ,đường Huỳnh Tấn Phát ,khu phố 7 ,thị trấn Nhà Bè ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A8='51/1A ,đường Huỳnh Tấn Phát ,khu phố 6 ,thị trấn Nhà Bè ,huyện Nhà Bè'

A9='519/9 ,đường Huỳnh Tấn Phát ,khu phố 7 ,thị trấn Nhà Bè ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A10='342/108 ,đường Huỳnh Tấn Phát ,khu phố 6 ,thị trấn Nhà Bè huyện Nhà Bè'

A11='B19-03 ,khu căn hộ  New  Sài Gòn ,ấp 5 ,xã Phước Kiển ,huyện Nhà Bè'

A12='24/2B ,khu phố 4 ,thị trấn Nhà Bè ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A13='18.6 ,lô D  ,chung cư P  ,ấp 3 ,xã Phú Xuân ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A14='280 đường Nguyễn Văn Tạo ,ấp 2 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh'
A141='trường trung học phổ thông Long Thới'
 
A15='92A  ,ấp 3 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A16='161 ,đường Lê Văn Lương ,ấp 5 ,xã Phước Kiển huyện Nhà Bè ,thành phố Hồ Chí Minh'

A17='34/7 ,khu phố 4 ,thị trấn Nhà Bè huyện Nhà Bè ,thành phố Hồ Chí Minh'
 
A18='64/6/35/2A ,đường Đào Tông Nguyên ,ấp 4 ,xã Phú Xuân ,huyện Nhà Bè thành ,phố Hồ Chí Minh'

A19='71/27 ,đường Nguyễn Văn Tạo ,ấp 1 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A20='133 ,Ấp 1 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A21='111/4A ,đường Lê Văn Lương ,ấp 3 ,xã Phước Kiển ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A22='12 ,lô A ,đường Nguyễn Văn Tạo ,ấp 1 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh '

A23='4/5 ,khu phố 5 ,thị trấn Nhà Bè ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A24='125 ,ấp 3 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A25='745 ,đường Nguyễn Văn Tạo ,ấp 1 ,xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A26='142 ,đường Huỳnh Tấn Phát ,thị trấn Nhà Bè ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A27='318 ,đường Nguyễn Văn Tạo ,ấp 2, xã Long Thới ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A28='9A ,ấp 5 ,xã Phước Kiển ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A29='01 ,ấp 3 ,xã Phước Kiển ,huyện Nhà Bè ,thành phố Hồ Chí Minh'

A30='A12-01 ,khu căn hộ New Sài Gòn F5 ,xã Phước Kiển ,huyện Nhà Bè '











"""

# số nhà
D1=re.findall(r'^\w+',A30)
print(D1)
def soNha(txt):
    so=re.findall(r'^\w+',txt)
    print("So nha : ",so)



print(soNha(A29))
#đường
#ấp
"""
aa=A29.find("ấp")
print(aa)


print(A29[aa:8])
"""

#
def lo(txt):
    loo=txt.find("lô")
    print(txt[loo:loo+4])
print(lo(A29))
#
def chung(txt):
    chungCu=txt.find("chung cư")
    print(txt[chungCu:chungCu+11])
print(chung(A29))
#
def truong(txt):
    truonghoc=txt.find("chung cư")
    print(txt[truonghoc:truonghoc+36])
print(chung(A29))
#

def khu(txt):
    khuCanho=txt.find("khu căn")
    print(txt[khuCanho:khuCanho+23])
print(khu(A29))
#
def duong(txt):
    duongg=txt.find("đường")
    print(txt[duongg:duongg+14])
print(duong(A29))
#
def ap(txt):
    app=txt.find("ấp")
    print(txt[app:app+4])
print(ap(A29))
#
def xa(txt):
    xaa=txt.find("xã")
    print(txt[xaa:xaa+13])
print(xa(A29))

#
def khuPho(txt):
    khupho=txt.find("khu phố ")
    print(txt[khupho:khupho+3])
print(khuPho(A29))
#
def thiTran(txt):
    thitran=txt.find("thị")
    print(txt[thitran:thitran+13])
print(thiTran(A29))
#

def huyen(txt):
    nhabe=txt.find("huyện")
    print(txt[nhabe:nhabe+12])
print(huyen(A29))
#thanh pho
thanhPho1=re.findall("th.*Minh$",A27)
print(thanhPho1)
def thanhPho(txt):
    pho=re.findall("th.*Minh$",txt)
    print("Thanh pho: ",pho)



"""



"""

print(s)
def ap(txt):
    app=re.findall(r'^s.*\d$',A29)
    print(app)
print(ap(A29))

#lo
print("lô A")
print("lô D")
#khu chungcu
print("chung cư P")
print("khu căn hộ New Sài Gòn")
print("khu căn hộ New Sài Gòn F5 ")
#truonghoc
print("trường trung học phổ thông Long Thới")
#duong
print("Lê Văn Lương")
print("Đào Sư Tích")
print("Huỳnh Tấn Phát")
print("Đào Tông Nguyên")
print("Nguyễn Văn Tạo")
#khu phố
print("khu phố 7")
print("khu phố 6")
print("khu phố 5")
#ap
print("ấp 3")
print("ấp 4")
print("ấp 5")
print("ấp 2")
print("ấp 1")


#xa

print("xã Phước Lộc")
print("xã Long Thới")
print("xã Phước Kiển")
print("xã Phú Xuân")

#thi tran
print("thị trấn Nhà Bè")
#huyen
print("huyện Nhà Bè")

s=u"ấp"

dd=re.findall(r'^s\s d$',A29)
print("huy: ",dd)

y=u"Bè"

huyen=re.findall(r'^huy.*y$',A30)
print("huyen: ",huyen)

import re

txt = "The rain in Spain"
x = re.findall("^The.*Spain$", txt)
print(x)



#thanh pho
thanhPho1=re.findall("th.*Minh$",A27)
print(thanhPho1)
def thanhPho(txt):
    pho=re.findall("th.*Minh$",txt)
    print("Thanh pho: ",pho)

print(thanhPho(A30))





s=u"ấp"

dd=re.findall(r'^s\s d$',A29)
print("ap: ",dd)

aa=A29.find("ấp")
print(aa)


print(A29[aa:8])





list=[A1,
      A2,
      A3,
      A4,
      A5,
      A6,
      A7,
      A8,
      A9,
      A10,
      A11,
      A12,
      A13,
      A14,
      A15,
      A16,
      A17,
      A18,
      A19,
      A20,
      A21,
      A22,
      A23,
      A24,
      A25,
      A26,
      A27,
      A28,
      A29,
      A30]
print(list)
L1="lô A"
L2="lô D"
K1="chung cư P"
K2="khu căn hộ New Sài Gòn"
K3="khu căn hộ New Sài Gòn F5 "
T1="trường trung học phổ thông Long Thới"
D1="Lê Văn Lương"
D2="Đào Sư Tích"
D3="Huỳnh Tấn Phát"
D4="Đào Tông Nguyên"
D5="Nguyễn Văn Tạo"
KP1="khu phố 7"
KP2="khu phố 6"
KP3="khu phố 5"
P1="ấp 1"
P2="ấp 2"
P3="ấp 3"
P4="ấp 4"
P5="ấp 5"
X1="xã Phước Lộc"
X2="xã Long Thới"
X3="xã Phước Kiển"
X4="xã Phú Xuân"
TT1="thị trấn Nhà Bè"
H1="huyện Nhà Bè"
def thanhPho(txt):
    pho=re.findall("th.*Minh$",txt)
    print("Thanh pho: ",pho)

if A7==thanhPho(A7):
    print("dung",A7)
else:
    print("sai")
txt=A1
def raSoat(txt): 
    if txt==L1:
        print("lo : ",L1)
    if txt==L2:
        print("lo : ",L2)
    if txt==K1:
        print(K1)
    if txt==K2:
        print(K2)
    if txt==K3:
        print(K3)
    if txt==T1:
        print(T1)
    if txt==D1:
        print(D1)
    if txt==D2:
        print(D2)
    if txt==D3:
        print(D3)
    if txt==D4:
        print(D4)
    if txt==D5:
        print(D5)
    if txt==KP1:
        print(KP1)
    if txt==KP2:
        print(KP2)
    if txt==KP3:
        print(KP3)
    if txt==P1:
        print(P1)
    if txt==P2:
        print(P2)
    if txt==P3:
        print(P3)
    if txt==P4:
        print(P4)
    if txt==P5:
        print(P5)
    if txt==X1:
        print(X1)
    if txt==X2:
        print(X2)
    if txt==X3:
        print(X3)
    if txt==X4:
        print(X4)
    if txt==TT1:
        print(TT1)
    if txt==H1:
        print(H1)
            
"""


    




















