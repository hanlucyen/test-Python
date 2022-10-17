"""
hướng dẫn in n hóa đơn với số lượng nhập từ bàn phím có sử dụng Propositional Logic
đầu tiên chúng ta xác định các thông tin cơ bản của một hóa đơn
+nơi mua
+hàng hóa
+số lượng
+đơn giá
+thành tiền
"""
import math
#tạo vòng lặp
while True:
    #chọn sản phẩm là rượu
    #bắt đầu tạo các thông tin liên quan
    name1="Rượu vang Ý 89 Primitivo Del Salento"
    price1=1350000
    print("Nhập số lượng mà khách mua rượu vang Ý 89: ")
    unit1=int(input())
    #tạo một điều kiện nhỏ cho sản phẩm này
    if unit1>=6:
        total1=unit1*price1
        price11=total1-(total1*0.1)
    else:
        total1=unit1*price1


    name2="Rượu vang Úc Penfolds BIN 123 SHIRAZ"
    price2=1380000
    print("Nhập số lượng mà khách đã mua rượu vang Úc: ")
    unit2=int(input())
    total2=unit2*price2

    name3="Rượu vang Chile LFE 900"
    price3=2090000
    print("Nhập số lượng mà khách đã mua rượu vang Chile: ")
    unit3=int(input())
    total3=unit3*price3

    name4="Rượu Vang Chile Montes Alpha M"
    price=5850000
    print("Nhập số lượng mà khách đã mua rượu vang Chile Montes Alpha M: ")
    unit4=int(input())
    total4=unit4*price4

    name5="Rượu vang Ý ZENATO Cresasso Corvina Veronese"
    price5=1600000
    print("Nhập số lượng khách đã mua rượu vang Ý ZENATO: ")
    unit5=int(input())
    total5=unit5*price5

    name6="Rượu vang Chile CONCHA y Toro Casillero del Diablo Reserva Privada"
    price6=490000
    print("Nhập số lượng khách đã mua rượu vang Chile CONCHA: ")
    unit6=int(input())
    if unit6>=6:
        total6=unit6*price6
        price62=total6-(total6*0.1)
    else:
        total6=unit6*price6
    #tổng sồ lượng đã mua
    unit=unit1+unit2+unit3+unit4+unit5+unit6
    #tổng tiền
    total=total1+total2+total3+total4+total5+total6
    #số tiền đã giảm giá
    if unit1>= 6 or unit6>=6:
        price=(price1*0.1)+(price6*0.1)
    #tạo 1 hàm nhập số hóa đơn
    print("Nhập số hóa đơn: ")
    n=input()





    #viết phần nội dung chính
    print("TIỆM RƯỢU WINE")
    print("Quốc lộ 1A,phường Linh Trung,thành phố Thủ Đức ,Thành phố Hồ Chí Minh")
    print("HÓA ĐƠN THANH TOÁN")
    print("Số hóa đơn :{}".format(n))
    from dtaetime import date
    today=date.today()
    print("Ngày: ",today)
    from datetime import datetime
    now=datetime.now()
    t=now.strftime("%H:%M:%S")
    print("Thời gian: ",t)
    print("Số thứ tự","Tên sản phẩm","Số lượng","Tiền")
    print("1",name1,unit1,price1)
    print("2",name2,unit2,price2)
    print("3",name3,unit3,price3)
    print("4",name4,unit4,price4)
    print("5",name5,unit5,price5)
    print("6",name6,unit6,price6)
    print("Tổng số lượng hàng hóa: ",unit)
    print("Thành tiền : ",total)
    print("Số tiền đã giảm: ",price)
    print("***********XIN HÂN HẠNH ĐƯỢC PHỤC VỤ QUÝ KHÁCH**********")
    # Vì đây là vòng lặp n lần nên sẽ tạo một điểm để dừng
    print("Vui lòng nhập n hoặc N để tiếp tục nhập")
    print("Vui lòng nhập y hoặc Y để dừng lại")
    w=input()
    if w=="n" or w=="N":
        print("Tiếp tục!")
    if w=="y" or w=="Y":
        break
    print(w)
print("Xin chào !")






    
