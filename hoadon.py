
import math
import os
from datetime import datetime
while True:
#tên nơi mua /công ty

#tiệm rượu  Sky

    print(" ","TIỆM RƯỢU SKY"," ")
#địa chỉ
"""
Quốc lộ 1A,phường Linh  Trung,thành phố Thủ Đức,thành phố Hồ Chí Minh
"""
    print("Quốc lộ 1A,phường Linh  Trung,\nthành phố Thủ Đức,thành phố Hồ Chí Minh")
# HÓA ĐƠN THANH TOÁN
"""
HÓA ĐƠN THANH TOÁN
"""
    print(" ","HÓA ĐƠN THANH TOÁN"," ")
#số hóa đơn
"""

giá trị bắt đầu là 1    :i=1
tăng dần đều 1 đơn vị   :i=i+1
"""
    import math
    print("nhap so n số hóa đơn : ")
    n=1
    n=int(input())
    

#ngày giờ
"""
in ngày hôm nay :   import datetime
                    date_object=datetime.date.today()
                    print(date_object)
giờ:            now=datetime.now()
                time = now.strftime("%H:%M:%S")
                print("time:", time)
"""
#ngày

    from datetime import date

    today = date.today()

    print("ngày:", today)

#giờ
    from datetime import datetime
    now = datetime.now()

    t = now.strftime("%H:%M:%S")
    print("time:", t)



#tên hàng -số lượng- đơn giá -thành tiền
#tên-số lượng- đơn giá
    name1 = 'Rượu vang Ý 89 Primitivo Del Salento'
    price1 = 1350000
    print("Nhập số lượng mà khách mua: ") 
    unit1 = int(input())
    if unit1 >=6:
    
        total1=unit1*price1
        print(total1)
        price11=total1-(total1*0.1)
        print("Giảm 10% pricel là: ",price11)
    else:
        total1=unit1*price1
        print(total1)

    name2 = 'Rượu vang Úc Penfolds BIN 128 SHIRAZ'
    price2 = 1380000
    print("Nhập số lượng mà khách mua: ") 
    unit2 = int(input())
    total2=unit2*price2
    print(total2)

    name3 = 'Rượu vang Chile Montes Alpha M'
    price3 = 2090000
    print("Nhập số lượng mà khách mua: ") 
    unit3 = int(input())
    total3=unit3*price3
    print(total3)




    name4 = 'Rượu vang Chile LFE 900'
    price4 = 585000
    print("Nhập số lượng mà khách mua: ") 
    unit4 = int(input())
    total4=unit4*price4
    print(total4)

    name5 = 'Rượu vang Ý ZENATO Cresasso Corvina Veronese'
    price5 = 1600000
    print("Nhập số lượng mà khách mua: ") 
    unit5 = int(input())
    total5=unit5*price5
    print(total5)

    name6 = 'Rượu vang CHile CONCHA y Toro \n                   Casillero del Diablo Reserva Privada'
    price6 = 490000
    print("Nhập số lượng mà khách mua: ") 
    unit6 = int(input())
    if unit6 >=6:
    
        total6=unit6*price6
        print(total6)
        price62=total6-(total6*0.1)
        print("Giảm 10% price6: ",price62)
    else:
        total6=unit6*price6
        print(total6)


#tính tiền

"""
print(" Vui lòng nhập name1,name2,name3,name4,name5,name6 tương ứng với sản phẩm quý khách muốn mua)
tenSanPhamDuocMua=int(input())

if tenSanPhamDuocMua in (name1,name2,name3,name4,name5,name6):
"""      
"""
name1 = 'orange'
price1 = 150
unit1 = 2

name2 = 'grape'
price2 = 130
unit2 = 23

tprice = price1 + price2
discount=15
fprice=tprice-discount

myformat = "{:<14}{:<25}{:<5}{}"
print(myformat.format('S.no', 'Product', 'Unit', 'Price'))
print(myformat.format('0', name1, unit1, price1))
print(myformat.format('1', name2, unit2, price2))
print(myformat.format('Discount: ', '', '', discount))
print(myformat.format('Total: ', '', '', fprice))
"""

#tổng cộng tổng số lượng hàng hóa đã mua   tổng thành tiền
    unit=unit1+unit2+unit3+unit4+unit5+unit6
    print(unit)
"""
print(myformat.format('
"""
#giảm % hóa đơn             số tiền đã giảm
    if unit1 >=6 or unit6 >=6:
        price=(price1*0.1+price6*0.1)
        print("Số tiền đã giảm: ",price)
    else:
        price=0
        print(price)
#tiền mặt            tiền ghi bằng số=tổng thành tiền-số tiền đã giảm
    total=total1  + total2  + total3 +total4 + total5 + total6
    print("Thành tiền : ",total)
    chu=str(total)
    print(len(chu))
#tiền ghi bằng chữ

"""

donvi = {0 : "không", 1 : "một", 2 : "hai", 3 : "ba", 4 : "bốn", 5 : "năm", 6 : "sáu", 7 : "bảy", 8 : "tám", 9 : "chín"}
hangmuoi = {10 : "mười", 11 : "mười một", 12 : "mười hai", 13 : "mười ba", 14 : "mười bốn", 15 : "mười lăm", 16 : "mười sáu", 17 : "mười bảy", 18 : "mười tám", 19 : "mười chín"}
hangchuc = {20 : "hai mươi", 30 : "ba mươi", 40 : "bốn mươi", 50 : "năm mươi", 60 : "sáu mươi", 70 : "bảy mươi", 80 : "tám mươi", 90 : "chín mươi"}
hangtram = {100 : "một trăm", 200 : "hai trăm", 300 : "ba trăm", 400 : "bốn trăm", 500 : "năm trăm", 600 : "sáu trăm", 700 : "bảy trăm", 800 : "tám trăm", 900 : "chín trăm"}
hangnghin={1000 : "một nghìn", 2000 : "hai nghìn ", 3000 : "ba nghìn", 4000 : "bốn nghìn", 5000 : "năm nghìn", 6000 : "sáu nghìn", 7000 : "bảy nghìn", 8000 : "tám nghìn", 9000 : "chín nghìn"}
hangchucnghin={10000 : "mười nghìn", 20000 : "hai mươi nghìn ", 30000 : "ba mươi nghìn", 40000 : "bốn mươi nghìn", 50000 : "năm mươi nghìn", 60000 : "sáu mươi nghìn", 70000 : "bảy mươi nghìn", 80000 : "tám mươi nghìn", 90000 : "chín mươi nghìn"}
hangtramnghin={100000 : "một trăm nghìn", 200000 : "hai trăm nghìn", 300000 : "ba trăm nghìn", 400000 : "bốn trăm nghìn", 500000 : "năm trăm nghìn", 600000 : "sáu trăm nghìn", 700000 : "bảy trăm nghìn", 800000 : "tám trăm nghìn", 900000 : "chín trăm nghìn"}
hangtrieu={1000000 : "một triệu", 2000000 : "hai triệu ", 3000000 : "ba triệu", 4000000 : "bốn triệu", 5000000 : "năm triệu", 6000000 : "sáu triệu", 7000000 : "bảy triệu", 8000000 : "tám triệu", 9000000 : "chín triệu"}
hangchuctrieu={10000000 : "mười triệu", 20000000 : "hai mươi triệu ", 30000000 : "ba mươi triệu", 40000000 : "bốn mươi triệu", 50000000 : "năm mươi triệu", 60000000 : "sáu mươi triệu", 70000000 : "bảy mươi triệu", 80000000 : "tám mươi triệu", 90000000 : "chín mươi triệu"}
print("Thành tiền : ",total)

if total < 10:
    print(donvi[total])
elif 10 <= total < 20:
    print(hangmuoi[total])
elif 20<= total < 100:
    if total % 10 == 0:
        print(hangchuc[total])
    else:
        print(hangchuc[total // 10 * 10], donvi[total %10])
else:
    print("and")
if len(chu)==8:
    if 10<= int(chu[0:1]) < 20:
        print(hangmuoi[chu[0:2]],"triệu")




"""

    myformat = "{:<14}{:<25}{:<5}{}"
    print('STT', 'Tên Sản Phẩm', '                                        ','Số Lượng','   ','Tiền')
    print('0','   ',  name1,'                     ', unit1, '   ', price1)
    print('1','   ',  name2,'                     ', unit2, '   ', price2)
    print('2','   ',  name3,'                           ', unit3, '   ', price3)
    print('3','   ',  name4,'                                  ', unit4, '   ', price4)
    print('4','   ',  name5,'             ', unit5, '   ', price5)
    print('5','   ',  name6,'                        ',unit6, '   ', price6)
    print('tổng số lượng hàng hóa: ', '','  ', '', unit)
    print('Số tiền đã giảm : ', '','    ', '', price,'Đồng')
    print('Thành tiền: ', '', '  ','', total,'Đồng')

"""
#xin hân hạnh được phục vụ quý khách
"""
    print("*****XIN HÂN HẠNH ĐƯỢC PHỤC VỤ QUÝ KHÁCH*****")
