"""
viết chương trình in hóa đơn với số liệu được nhập từ bàn phím
đầu tiên phải xác định các thông tin cơ bản của một hóa đơn
+nơi mua
+thời gian(ngày +giờ)
+sản phẩm
+đơn giá
+số lượng
+ thành tiền

"""
import math
while True:
    #chọn các thông tin liên quan đến sản phẩm
    #chọn sản phẩm là rượu
    name1 = 'Rượu vang Ý 89 Primitivo Del Salento'
    price1 = 1350000
    print("Nhập số lượng mà khách mua rượu vang Ý 89 Primitivo Del Salento: ") 
    unit1 = int(input())
    if unit1 >=6:
    
        total1=unit1*price1
        price11=total1-(total1*0.1)# mặt hàng này giảm 10%
       
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
    
    # viết công thức tính tổng số lượng , giảm giá,thành tiền
     #tổng số lượng   
    unit=unit1+unit2+unit3+unit4+unit5+unit6
     #tổng giảm giá
    if unit1 >=6 or unit6 >=6:
        price=(price1*0.1+price6*0.1)
    #tổng tiền phải trả
    total=total1+total2+total3+total4+total5+total6
    #viết một dòng cho số hóa đơn
    print("Nhập số hóa đơn: ")
    n=input()
    
    # bắt đầu viết phần nội dung in ra của một hóa đơn
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("TIỆM RƯỢU WINE")
    print("Quốc lộ 1A,phường Linh Trung,thành phố Thủ Đức,thành phố Hồ Chí Minh")
    print(" ","HÓA ĐƠN THANH TOÁN"," ")
    print("Số hóa đơn : {}".format(n))

    #ngày
    from datetime import date
    today=date.today()
    print("Ngày: ",today)
    #giờ
    from datetime import datetime
    now=datetime.now()
    t=now.strftime("%H:%M:%S")
    print("Giờ: ",t)
    #viết in các thông tin của sản phẩm
    print('STT','   ', 'Tên Sản Phẩm', '                                        ','Số Lượng','   ','Tiền')
    print('0','   ',  name1,'                     ', unit1, '   ', price1)
    print('1','   ',  name2,'                     ', unit2, '   ', price2)
    print('2','   ',  name3,'                           ', unit3, '   ', price3)
    print('3','   ',  name4,'                                  ', unit4, '   ', price4)
    print('4','   ',  name5,'             ', unit5, '   ', price5)
    print('5','   ',  name6,'                        ',unit6, '   ', price6)
    print('Tổng số lượng hàng hóa đã mua: ', '','  ', '', unit)
    print('Số tiền đã giảm : ', '','    ', '', price,'Đồng')
    print('Thành tiền: ', '', '  ','', total,'Đồng')
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    #vì ban đầu tạo vòng lặp while True : để tạo n hóa đơn nên bây giờ viết thêm một lệnh để dừng chương trình in hóa đơn
    #tạo điều kiện dừng
    print("Nếu muốn tiếp tục in hóa đơn vui lòng nhập :y hoặc Y")
    print("Nếu muốn kết thúc việc in hóa đơn vui lòng nhập : n hoặc N")
    
    w=input()
    if w=="y" or w=="Y":
        print("Mời nhập tiếp!")
    if w=="n" or w=="N":
        break
    print(w)
print("Thoát!")

    
    
