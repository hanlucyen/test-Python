import math
#math.asin(30)  vi sin() la gia tri tu (-1;1) neu vuot qua se error
goc_do=math.radians(math.sin(30)) # or goc_do=math.pi/6
print('gia tri cua goc tinh theo do: ',goc_do)
#gia tri chinh xac cua sin(60) la 0.5 nam trong khoang(-1;1)
goc_rad=math.radians(30)
print('gia tri cua goc theo radian: ',goc_rad)
#doi do sang radian ta co cong thuc . radian=do*(pi/180)
radian=goc_do*(math.pi)/180
print('gia tri sin cua goc theo don vi radian bang lenh math.sin: ',radian)
