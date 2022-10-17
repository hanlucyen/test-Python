pip install opencv-contrib-python --upgrade
pip install opencv-python 
import cv2
facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("h1.png")
imgGray=cv2.cvtColor(img, cv2.COOLOR_BGR2GRAY)
faces=facecascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2)
cv2.imshow("Result",img)
cv2.waitKey(0)
import cv2

#tai thu vien anh(file.xml vao)

facecascade=cv2.CascadeClassifier("downloads:\haarcascade_frontalface_default.xml")

#doc anh
find="data"+"/"
find=find.replace("\\","/")
#img=cv2.imread(find+"h1.png")
#img=cv2.imread(find+"h1.png")
img=cv2.imread(r"downloads:\h1.png")
#chuyen anh thanh grayscale
imgGray=cv2.cvtColor(img, cv2.COOLOR_BGR2GRAY)
#nhat dien khuong mat va ve hinhf chu nhat xung quanh
faces=facecascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2)
#in ket qua
cv2.imshow("Result",img)
cv2.waitKey(0)
