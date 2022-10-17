print("Change file large number of name according to a rule bar!")
import os
import zipfile
jungle_zip = zipfile.ZipFile("C:\\Users\\ASUS\\Downloads\\fileRename.zip", "w")# gọi chơi
print(jungle_zip)

os.chdir('C:/Users/ASUS/Desktop/fileRename/phongcanh')

print(os.getcwd())#vào thư mục làm việc
COUNT=1# giá trị đếm tăng dần
def increment():
    global COUNT
    COUNT=COUNT+1

for f in os.listdir():
    f_name, f_ext=os.path.splitext(f)# tách phần đuôi và phần tên
    f_name='Phongcanh_' +str(COUNT).zfill(2)
    increment()#thực hiện tăng tiến biến count lên 1 đơn vị

    new_name='{}{}'.format(f_name, f_ext)
    os.rename(f,new_name)
