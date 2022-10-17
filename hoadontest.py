import math
import os
from datetime import datetime
while True:
    name1 = 'Rượu vang Ý 89 Primitivo Del Salento'
    price1 = 1350000
    print("Nhập số lượng mà khách mua rượu vang Ý 89 Primitivo Del Salento: ") 
    unit1 = int(input())
    if unit1 >=6:
    
        total1=unit1*price1
        print(total1)
        price11=total1-(total1*0.1)
       
    else:
        total1=unit1*price1
        

    name2 = 'Rượu vang Úc Penfolds BIN 128 SHIRAZ'
    price2 = 1380000
    print("Nhập số lượng mà khách mua rượu vang Úc Penfolds BIN 128 SHIRAZ: ") 
    unit2 = int(input())
    total2=unit2*price2
    

    name3 = 'Rượu vang Chile Montes Alpha M'
    price3 = 2090000
    print("Nhập số lượng mà khách mua rượu vang Chile Montes Alpha M: ") 
    unit3 = int(input())
    total3=unit3*price3
    



    name4 = 'Rượu vang Chile LFE 900'
    price4 = 585000
    print("Nhập số lượng mà khách mua rượu vang Chile LFE 900: ") 
    unit4 = int(input())
    total4=unit4*price4
 

    name5 = 'Rượu vang Ý ZENATO Cresasso Corvina Veronese'
    price5 = 1600000
    print("Nhập số lượng mà khách mua rượu vang Ý ZENATO Cresasso Corvina Veronese: ") 
    unit5 = int(input())
    total5=unit5*price5
    

    name6 = 'Rượu vang Chile CONCHA y Toro \n   Casillero del Diablo Reserva Privada'
    price6 = 490000
    print("Nhập số lượng mà khách mua rượu vang Chile CONCHA : ") 
    unit6 = int(input())
    if unit6 >=6:
    
        total6=unit6*price6
        print(total6)
        price62=total6-(total6*0.1)
        
    else:
        total6=unit6*price6
        
    unit=unit1+unit2+unit3+unit4+unit5+unit6
    
    if unit1 >=6 or unit6 >=6:
        price=(price1*0.1+price6*0.1)
       
    else:
        price=0
    total=total1  + total2  + total3 +total4 + total5 + total6
    print("nhập số hóa đơn : ")
   
    n=int(input())
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

    print(" ","TIỆM RƯỢU WINE"," ")
    print("Quốc lộ 1A,phường Linh  Trung,\nthành phố Thủ Đức,thành phố Hồ Chí Minh")
    print(" ","HÓA ĐƠN THANH TOÁN"," ")
   
    print("nhập số hóa đơn : {}".format(n))
    from datetime import date

    today = date.today()

    print("ngày:", today)
    from datetime import datetime
    now = datetime.now()

    t = now.strftime("%H:%M:%S")
    print("time:", t)
            
    
    
    
    myformat = "{:<14}{:<25}{:<5}{}"
    print('STT','   ', 'Tên Sản Phẩm', '                                        ','Số Lượng','   ','Tiền')
    print('0','   ',  name1,'                     ', unit1, '   ', price1)
    print('1','   ',  name2,'                     ', unit2, '   ', price2)
    print('2','   ',  name3,'                           ', unit3, '   ', price3)
    print('3','   ',  name4,'                                  ', unit4, '   ', price4)
    print('4','   ',  name5,'             ', unit5, '   ', price5)
    print('5','   ',  name6,'                        ',unit6, '   ', price6)
    print('Tổng số lượng hàng hóa: ', '','  ', '', unit)
    print('Số tiền đã giảm : ', '','    ', '', price,'Đồng')
    print('Thành tiền: ', '', '  ','', total,'Đồng')
    print("                 *****XIN HÂN HẠNH ĐƯỢC PHỤC VỤ QUÝ KHÁCH*****")

    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("Nếu muốn tiếp lại vui lòng nhập : y hoặc Y")
    print("Nếu muốn dừng lại vui lòng nhập : n hoặc N")
    w=input()
    if w=="y" or w=="Y":
        print("Mời nhập tiếp!")
    if w=="n" or w=="N":
        break
    print(w)
    
print("Thoát!")
        
