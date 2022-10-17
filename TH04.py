"""
#câu 1
print("Hãy nhập nội dung tại đây:")
n=input()
print("Chuỗi ký tự đã nhập là: ",n)
print("Độ dài chuỗi vừa nhập: ",len(n))
print("Số lượng ký tự in hoa là: ", sum(1 for c in n if c.isupper()))
print("Số lượng ký tự in thường là:",sum(1 for c in n if c.islower()))
print("Chuỗi viết hoa toàn bộ là: ",n.upper())

#câu 2
while True:
    print("Hãy nhập vào một câu có nghĩa trong tiếng Anh\n (ta dùng tiếng Anh đễ tránh xảy ra lỗi ra thao tác với mã hóa tiếng Việt):")
    x=input()
    print("In nội dung vừa nhập:",x)
    print(" Nhập số tại vị trí bắt đầu lấy chuỗi thay thế:")
    i=int(input())
    print(" Nhập số tại vị trí kết thúc chuỗi thay thế:")
    j=int(input())
    print("Nhập từ muốn thay thế (từ A) và từ sẽ được dùng để thay thế (từ b): ")
    y=input()
    print("In chuỗi thay thế của x: ",x.replace(x[i:j],y))
    print(" Nhập lại một phần của chuỗi x để thực hiện tìm kíếm : ")
    z=input()
    print(" Thực hiện tìm kiếm z trong chuỗi x được giá trị trả về có độ dài là: ",x.find(z))
    print("\n")
    print("\n")
print("\n")
    print("Bạn có muốn nhập tiếp không!")
    print("nhập y hoặc Y để tiếp tục!")
    print("Nhập n hoặc N để thoát khỏi chưa trình!")
    w=input()
    if w=="y" or w=="Y":
        print("Mời nhập tiếp!")
    if w=="n" or w=="N":
        break
    print(w)
print("THOÁT!")
"""



