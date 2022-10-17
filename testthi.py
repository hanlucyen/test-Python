from scipy import linalg
import numpy as np
#khởi tạo ma trận
a=np.array([1,2,3])
b=np.array([(1+9j,2j,3j),(4j,5j,6j)])
c=np.array([[(0.5,1.5,10),(3,2,1)],[(6,5,4),(7,8,9)]])
#Các kiểu khai báo và khởi tạo ma trận
A=np.matrix(np.random.random((2,2)))
B=np.asmatrix(b)
C=np.mat(np.random.random((10,5)))
D=np.mat([[4,3],[2,6]])
#các hàm trên ma trận
M1=np.add(A,D)
M2=np.subtract(A,D)
M3=np.divide(A,D)
M4=A@D
M5=np.multiply(D,A)
M6=np.vdot(A,D)
M7=linalg.expm(A)
M8=linalg.logm(A)
print("M1= ",M1)
print("M2= ",M2)
print("M3= ",M3)
print("M4= ",M4)
print("M5= ",M5)
print("M6= ",M6)
print("M7= ",M7)
print("M8= ",M8)
