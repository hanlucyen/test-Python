
def nhap_canh():
    """Hàm yêu cầu nhập điểm và trả về giá trị trung bình"""
    # Bước 1: Nhập dữ liệu
    print("Nhập a: ")
    a = float(input())
 
    print("Nhập b: ")
    b = float(input())
 
    print("Nhập c: ")
    c = float(input())
 
    # Bước 2: Tính điểm trung bình
    tong = a+b
 
    return tong
 
 
def kiem_tra_tam_giac(c):
    """Hàm in kết quả lên màn hình"""
    print("Điểm trung bình là: ", tong)
    if (c<tong):
        print("Học lực yếu")
    elif (c>tong):
        print("Học lực yếu")
    elif (c==0):
        print("Học lực giỏi")
 
 
# Sử dụng hàm
tong = nhap_canh()
kiem_tra_tam_giac(tong)
print(kiem_tra_tam_giac(tong))
