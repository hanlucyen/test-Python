print("BAO BÚA KÉO")
print("Vui lòng chọn ký hiệu cho đúng nha.")
print("Nếu chọn kí hiệu bao vui lòng nhập b1")
print("Nếu chọn kí hiệu búa vui lòng nhập b2")
print("Nếu chọn kí hiệu kéo vui lòng nhập k")
nhap=input()
mylist=["b1","b2","k"]


import random
from random import randint

#if nhap!="b1" or nhap!="b2" or nhap!="k":
#print("END")
computer=random.choice(mylist)
print("Kí hiệu mà máy tính chọn: ",computer)

"""
if computer=="b1":
    computer="b1"
if computer=="b2":
    computer="b2"
if computer=="k":
    computer="k"
print("Kết quả của máy chọn: "+computer)
"""
for value in mylist:
    if value!=nhap:
        print("Vui lòng Nhập!")
        print("Nếu chọn kí hiệu bao vui lòng nhập b1")
        print("Nếu chọn kí hiệu búa vui lòng nhập b2")
        print("Nếu chọn kí hiệu kéo vui lòng nhập k")
        nhap=input()
        mylist=["b1","b2","k"]


import random
from random import randint

#if nhap!="b1" or nhap!="b2" or nhap!="k":
#print("END")
computer=random.choice(mylist)
print("Kí hiệu mà máy tính chọn: ",computer)
    

if computer==nhap:
    print("Hòa")
else:
    if nhap=="b1":
        if computer=="b2":
            print("Chúc mừng bạn đã chiến thắng!")
        else:
            print("Thật tiếc quá! Bạn thua rồi!")
    elif nhap=="b2":
        if computer=="k":
            print("Chúc mừng bạn đã chiến thắng!")
        else:
            print("Thật tiếc quá! Bạn thua rồi!")
    elif nhap=="k":
        if computer=="b2":
            print("Chúc mừng bạn đã chiến thắng!")
        else:
            print("Thật tiếc quá! Bạn thua rồi!")
    
"""
if nhap==b1 and computer==b1:
    print("Hòa!")
if nhap==b1 and computer==b2:
    print("Chúc mừng bạn!")
if nhap==b1 and computer==k:
    print("Thật tiếc quá!")
if nhap==b2 and computer==b1:
    print("Thật tiếc quá!")
if nhap==b2 and computer==b2:
    print("Hòa!")
if nhap==b2 and computer==k:
    print("Chúc mừng bạn!")
if nhap==k and computer==b1:
    print("Chúc mừng bạn!")
if nhap==k and computer==b2:
    print("Thật tiếc quá!")
if nhap==k and computer==k:
    print("Hòa!")
    
    
"""
