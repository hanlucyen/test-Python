import numpy as np
A=np.array([[1,1,0,0,1],
   [3,1,0,1,1],
   [5,2,0,1,2],
   [2,0,1,2,3]])
B=np.array([[1,1,2,2,1],
   [2,2,2,0,2],
   [0,1,2,4,2],
   [1,4,1,2,2]])
C=np.array([[0,5,1,1,1],
   [0,1,1,1,3],
   [1,3,1,3,1],
   [0,1,3,3,0]])
D=np.array([[3,1,1,0,1],
   [5,0,0,3,7],
   [7,0,0,3,5],
   [5,0,3,5,3]])
E=np.array([[0,0,0,10,0],
   [0,0,15,0,0],
   [0,5,15,5,0],
   [0,20,5,0,0]])
print(E)
#An toàn trong chiến dịch ngắn hạn 1-2 ngày (có yếu tố tránh lộ bí mật; không quan tâm đến các yếu tố khác);
print('An toàn trong chiến dịch ngắn hạn 1-2 ngày (có yếu tố tránh lộ bí mật; không quan tâm đến các yếu tố khác);')
a=0
if E[0][0]<=0:
    print('nhan E[0][0]')
else:
    print('loai', E[0][0])
if E[0][1]<=0:
    print('nhan E[0][1]')
else:
    print('loai', E[0][1])
if E[0][2]<=0:
    print('nhan E[0][2]')
else:
    print('loai', E[0][2])
if E[0][3]<=0:
    print('nhan E[0][3]')
else:
    print('loai', E[0][3])
if E[0][4]<=0:
    print('nhan E[0][4]')
else:
    print('loai', E[0][4])
if E[1][0]<=0:
    print('nhan E[1][0]')
else:
    print('loai', E[1][0])
if E[2][0]<=0:
    print('nhan E[2][0]')
else:
    print('loai', E[2][0])
if E[3][0]<=0:
    print('nhan E[3][0]')
else:
    print('loai', E[3][0])
if E[1][1]<=0:
    print('nhan E[1][1]')
else:
    print('loai', E[1][1])
if E[1][2]<=0:
    print('nhan E[1][2]')
else:
    print('loai',E[1][2])
if E[1][3]<=0:
    print('nhan E[1][3]')
else:
    print('loai',E[1][3])
if E[1][4]<=0:
    print('nhan E[1][4]')
else:
    print('loai',E[1][4])
if E[2][1]<=0:
    print('nhan E[2][1]')
else:
    print('loai',E[2][1])
if E[3][1]<=0:
    print('nhan E[3][1]')
else:
    print('loai',E[3][1])
if E[2][2]<=0:
    print('nhan E[2][2]')
else:
    print('loai',E[2][2])
if E[2][3]<=0:
    print('nhan E[2][3]')
else:
    print('loai',E[2][3])
if E[2][4]<=0:
    print('nhan E[2][4]')
else:
    print('loai',E[2][4])
if E[3][2]<=0:
    print('nhan E[3][2]')
else:
    print('loai',E[3][2])
if E[3][3]<=0:
    print('nhan E[3][3]')
else:
    print('loai',E[3][3])
if E[3][4]<=0:
    print('nhan E[3][4]')
else:
    print('loai',E[3][4])
#An toàn trong tập luyện thời bình (không cần xét yếu tố tránh lộ bí mật và bệnh dịch).
print('An toàn trong tập luyện thời bình (không cần xét yếu tố tránh lộ bí mật và bệnh dịch).')
a=0
b=0
c=0
if A[0][0] and B[0][0] and C[0][0]<=0:
    print('nhan A[0][0] B[0][0] C[0][0]')
else:
    print('loai',A[0][0])
if A[0][1]and B[0][1] and C[0][1]<=0:
    print('nhan ABC[0][1]')
else:
    print('loai',A[0][1])
if A[0][2]and B[0][2] and C[0][2]<=0:
    print('nhan ABC[0][2]')
else:
    print('loai',A[0][2])
if A[0][3]and B[0][3] and C[0][3]<=0:
    print('nhan ABC[0][3]')
else:
    print('loai',A[0][3])
if A[0][4]and B[0][4] and C[0][4]<=0:
    print('nhan ABC[0][4]')
else:
    print('loai',A[0][4])
if A[1][0]and B[1][0] and C[1][0]<=0:
    print('nhan ABC[1][0]')
else:
    print('loai',A[1][0])
if A[2][0]and B[2][0] and C[2][0]<=0:
    print('nhan ABC[2][0]')
else:
    print('loai',A[2][0])
if A[3][0]and B[3][0] and C[3][0]<=0:
    print('nhan ABC[3][0]')
else:
    print('loai',A[3][0])
if A[1][1]and B[1][1] and C[1][1]<=0:
    print('nhan ABC[1][1]')
else:
    print('loai',A[1][1])
if A[1][2]and B[1][2] and C[1][2]<=0:
    print('nhan ABC[1][2]')
else:
    print('loai',A[1][2])
if A[1][3]and B[1][3] and C[1][3]<=0:
    print('nhan ABC[1][3]')
else:
    print('loai',A[1][3])
if A[1][4]and B[1][4] and C[1][4]<=0:
    print('nhan ABC[1][4]')
else:
    print('loai',A[1][4])
if A[2][1]and B[2][1] and C[2][1]<=0:
    print('nhan ABC[2][1]')
else:
    print('loai',A[2][1])
if A[3][1]and B[3][1] and C[3][1]<=0:
    print('nhan ABC[3][1]')
else:
    print('loai',A[3][1])
if A[2][2]and B[2][2] and C[2][2]<=0:
    print('nhan ABC[2][2]')
else:
    print('loai',A[2][2])
if A[2][3]and B[2][3] and C[2][3]<=0:
    print('nhan ABC[2][3]')
else:
    print('loai',A[2][3])
if A[2][4]and B[2][4] and C[2][4]<=0:
    print('nhan ABC[2][4]')
else:
    print('loai',A[2][4])
if A[3][2]and B[3][2] and C[3][2]<=0:
    print('nhan ABC[3][2]')
else:
    print('loai',A[3][2])
if A[3][3]and B[3][3] and C[3][3]<=0:
    print('nhan ABC[3][3]')
else:
    print('loai',A[3][3])
if A[3][4]and B[3][4] and C[3][4]<=0:
    print('nhan ABC[3][4]')
else:
    print('loai',A[3][4])
#An toàn theo mùa khô (không có lũ, không sạt núi nhưng có cháy rừng và bệnh dịch)
print('An toàn theo mùa khô (không có lũ, không sạt núi nhưng có cháy rừng và bệnh dịch)')
a=0
d=0
if A[0][0] and D[0][0]<=0:
    print('nhan E[0][0]')
else:
    print('loai', E[0][0])
if A[0][1]and D[0][0]<=0:
    print('nhan E[0][1]')
else:
    print('loai', E[0][1])
if A[0][2]and D[0][0]<=0:
    print('nhan E[0][2]')
else:
    print('loai', E[0][2])
if A[0][3]and D[0][0]<=0:
    print('nhan E[0][3]')
else:
    print('loai', E[0][3])
if A[0][4]and D[0][0]<=0:
    print('nhan AD[0][4]')
else:
    print('loai', E[0][4])
if A[1][0]and D[1][0]<=0:
    print('nhan AD[1][0]')
else:
    print('loai', E[1][0])
if A[2][0]and D[2][0]<=0:
    print('nhan AD[2][0]')
else:
    print('loai', E[2][0])
if A[3][0]and D[3][0]<=0:
    print('nhan AD[3][0]')
else:
    print('loai', E[3][0])
if A[1][1]and D[1][1]<=0:
    print('nhan AD[1][1]')
else:
    print('loai', E[1][1])
if A[1][2]and D[1][2]<=0:
    print('nhan AD[1][2]')
else:
    print('loai',E[1][2])
if A[1][3]and D[1][3]<=0:
    print('nhan AD[1][3]')
else:
    print('loai',E[1][3])
if A[1][4]and D[1][4]<=0:
    print('nhan AD[1][4]')
else:
    print('loai',E[1][4])
if A[2][1]and D[2][1]<=0:
    print('nhan AD[2][1]')
else:
    print('loai',E[2][1])
if A[3][1]and D[3][1]<=0:
    print('nhan AD[3][1]')
else:
    print('loai',E[3][1])
if A[2][2]and D[2][2]<=0:
    print('nhan AD[2][2]')
else:
    print('loai',E[2][2])
if A[2][3]and D[2][3]<=0:
    print('nhan AD[2][3]')
else:
    print('loai',E[2][3])
if A[2][4]and D[2][4]<=0:
    print('nhan AD[2][4]')
else:
    print('loai',E[2][4])
if A[3][2]and D[3][2]<=0:
    print('nhan AD[3][2]')
else:
    print('loai',E[3][2])
if A[3][3]and D[3][3]<=0:
    print('nhan AD[3][3]')
else:
    print('loai',E[3][3])
if A[3][4]and D[3][4]<=0:
    print('nhan AD[3][4]')
else:
    print('loai',E[3][4])
#An toàn trong mùa mưa (có lũ, có lỡ núi, có bệnh dịch mà không có cháy rừng).
print('An toàn trong mùa mưa (có lũ, có lỡ núi, có bệnh dịch mà không có cháy rừng).')
b=0
c=0
d=0
if B[0][0] and D[0][0] and C[0][0]<=0:
    print('nhan D[0][0] B[0][0] C[0][0]')
else:
    print('loai',B[0][0])
if B[0][1]and D[0][1] and C[0][1]<=0:
    print('nhan BCD[0][1]')
else:
    print('loai',B[0][1])
if B[0][2]and D[0][2] and C[0][2]<=0:
    print('nhan BCD[0][2]')
else:
    print('loai',B[0][2])
if B[0][3]and D[0][3] and C[0][3]<=0:
    print('nhan BCD[0][3]')
else:
    print('loai',B[0][3])
if B[0][4]and D[0][4] and C[0][4]<=0:
    print('nhan BCD[0][4]')
else:
    print('loai',B[0][4])
if B[1][0]and D[1][0] and C[1][0]<=0:
    print('nhan BCD[1][0]')
else:
    print('loai',B[1][0])
if B[2][0]and D[2][0] and C[2][0]<=0:
    print('nhan BCD[2][0]')
else:
    print('loai',B[2][0])
if B[3][0]and D[3][0] and C[3][0]<=0:
    print('nhan BCD[3][0]')
else:
    print('loai',B[3][0])
if B[1][1]and D[1][1] and C[1][1]<=0:
    print('nhan BCD[1][1]')
else:
    print('loai',B[1][1])
if B[1][2]and D[1][2] and C[1][2]<=0:
    print('nhan BCD[1][2]')
else:
    print('loai',B[1][2])
if B[1][3]and D[1][3] and C[1][3]<=0:
    print('nhan BCD[1][3]')
else:
    print('loai',B[1][3])
if B[1][4]and D[1][4] and C[1][4]<=0:
    print('nhan BCD[1][4]')
else:
    print('loai',B[1][4])
if B[2][1]and D[2][1] and C[2][1]<=0:
    print('nhan BCD[2][1]')
else:
    print('loai',B[2][1])
if B[3][1]and D[3][1] and C[3][1]<=0:
    print('nhan BCD[3][1]')
else:
    print('loai',B[3][1])
if B[2][2]and D[2][2] and C[2][2]<=0:
    print('nhan BCD[2][2]')
else:
    print('loai',B[2][2])
if B[2][3]and D[2][3] and C[2][3]<=0:
    print('nhan BCD[2][3]')
else:
    print('loai',B[2][3])
if B[2][4]and D[2][4] and C[2][4]<=0:
    print('nhan BCD[2][4]')
else:
    print('loai',B[2][4])
if B[3][2]and D[3][2] and C[3][2]<=0:
    print('nhan BCD[3][2]')
else:
    print('loai',B[3][2])
if B[3][3]and D[3][3] and C[3][3]<=0:
    print('nhan BCD[3][3]')
else:
    print('loai',B[3][3])
if B[3][4]and D[3][4] and C[3][4]<=0:
    print('nhan BCD[3][4]')
else:
    print('loai',B[3][4])
#An toàn trong 8 tháng (có đủ các mùa và có yếu tố tránh lộ bí mật)
print('An toàn trong 8 tháng (có đủ các mùa và có yếu tố tránh lộ bí mật)')
a=0
b=0
c=0
d=0
e=0
if A[0][0] and B[0][0] and C[0][0] and D[0][0] and E[0][0]<=0:
    print('nhan A[0][0] B[0][0] C[0][0]')
else:
    print('loai',A[0][0])
if A[0][1]and B[0][1] and C[0][1]and D[0][1] and E[0][1]<=0:
    print('nhan ABC[0][1]')
else:
    print('loai',A[0][1])
if A[0][2]and B[0][2] and C[0][2]and D[0][2] and E[0][2]<=0:
    print('nhan ABC[0][2]')
else:
    print('loai',A[0][2])
if A[0][3]and B[0][3] and C[0][3]and D[0][3] and E[0][3]<=0:
    print('nhan ABC[0][3]')
else:
    print('loai',A[0][3])
if A[0][4]and B[0][4] and C[0][4]and D[0][0] and E[0][0]<=0:
    print('nhan ABC[0][4]')
else:
    print('loai',A[0][4])
if A[1][0]and B[1][0] and C[1][0]and D[1][0] and E[1][0]<=0:
    print('nhan ABC[1][0]')
else:
    print('loai',A[1][0])
if A[2][0]and B[2][0] and C[2][0]and D[2][0] and E[2][0]<=0:
    print('nhan ABC[2][0]')
else:
    print('loai',A[2][0])
if A[3][0]and B[3][0] and C[3][0]and D[3][0] and E[3][0]<=0:
    print('nhan ABC[3][0]')
else:
    print('loai',A[3][0])
if A[1][1]and B[1][1] and C[1][1]and D[1][1] and E[1][1]<=0:
    print('nhan ABC[1][1]')
else:
    print('loai',A[1][1])
if A[1][2]and B[1][2] and C[1][2]and D[1][2] and E[1][2]<=0:
    print('nhan ABC[1][2]')
else:
    print('loai',A[1][2])
if A[1][3]and B[1][3] and C[1][3]and D[1][3] and E[1][3]<=0:
    print('nhan ABC[1][3]')
else:
    print('loai',A[1][3])
if A[1][4]and B[1][4] and C[1][4]and D[1][4] and E[1][4]<=0:
    print('nhan ABC[1][4]')
else:
    print('loai',A[1][4])
if A[2][1]and B[2][1] and C[2][1]and D[2][1] and E[2][1]<=0:
    print('nhan ABC[2][1]')
else:
    print('loai',A[2][1])
if A[3][1]and B[3][1] and C[3][1]and D[3][1] and E[3][1]<=0:
    print('nhan ABC[3][1]')
else:
    print('loai',A[3][1])
if A[2][2]and B[2][2] and C[2][2]and D[2][2] and E[2][2]<=0:
    print('nhan ABC[2][2]')
else:
    print('loai',A[2][2])
if A[2][3]and B[2][3] and C[2][3]and D[2][3] and E[2][3]<=0:
    print('nhan ABC[2][3]')
else:
    print('loai',A[2][3])
if A[2][4]and B[2][4] and C[2][4]and D[2][4] and E[2][4]<=0:
    print('nhan ABC[2][4]')
else:
    print('loai',A[2][4])
if A[3][2]and B[3][2] and C[3][2]and D[3][2] and E[3][2]<=0:
    print('nhan ABC[3][2]')
else:
    print('loai',A[3][2])
if A[3][3]and B[3][3] and C[3][3]and D[3][3] and E[3][3]<=0:
    print('nhan ABC[3][3]')
else:
    print('loai',A[3][3])
if A[3][4]and B[3][4] and C[3][4]and D[3][4] and E[3][4]<=0:
    print('nhan ABC[3][4]')
else:
    print('loai',A[3][4])



