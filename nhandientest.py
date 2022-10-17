"""
import cv2


# Load the cascade
facecascade=cv2.CascadeClassifier("C:\\Users\\ASUS\\Documents\\python\\master.xml")
# Read the input image
img=cv2.imread("C:\\Users\\ASUS\\Downloads\\h1.png")
#imgResize=cv2.resize(img,(300,450))

# Convert into grayscale
imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces=facecascade.detectMultiScale(imgGray,1.1,4)
# Draw rectangle around the faces
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# Display the output
cv2.imshow("Result",img)
cv2.waitKey(0)

#thay bao tui nhap cai nay tý nha# ngô ta :))
# đc roi đo
#copy vao duoc khong 
# doi chut nhe
"""
import cv2

# Tai thu vien (file .xml vao)
taptin_xml = r"C:\Users\ASUS\Downloads\haarcascade_frontalface_default.xml" #them duong dan 
facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#xin phep thu cai nay 1 ty 
#luc nay thay noi tui nen go 2 \\ nhung thu roi error
# Doc anh:
tm_anh = "data" + "/"
tm_anh = tm_anh.replace("\\", "/")  ####XOOONG doi chut
#img=cv2.imread(tm_anh + "hoahau1.png")
#img=cv2.imread(tm_anh + "hoahau2.jpg")
img=cv2.imread(r"C:\Users\ASUS\Downloads\moinguoi.png") #ban them duong dn a
#img=cv2.imread(tm_anh + "khoaHTTTVT4.png")
#img=cv2.imread(tm_anh + "hcmgis2015.jpg")


# Chuyen thanh grayscale:
imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Nhan dien khuon mat va ve hinh chu nhat xung quanh:
faces = facecascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# Hien thi ra ket qua
print('Số khuôn mặt: ',len(faces))
cv2.imshow("Ket qua la:",img)
cv2.waitKey(0)
