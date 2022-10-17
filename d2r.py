import math
#math.asin(60) error vi sin() la gia tri tu (-1;1) neu vuot qua se error
#gia tri chinh xac cua sin(60) la sqrt(3)/2 nam trong khoang(-1;1)
goc_do=math.sqrt(3)/2 # or goc_do=math.pi/3
print('gia tri cua goc tinh theo do: ',goc_do)
#doi do sang radian ta co cong thuc . radian=do*(pi/180)
radian=goc_do*(math.pi)/180
print('gia tri cua goc theo radian: ',radian)
