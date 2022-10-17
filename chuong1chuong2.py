Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tính toán cơ bản
>>> 3+4
7
>>> 4-7
-3
>>> 7*3
21
>>> 4-7*3
-17
>>> 21/3
7.0
>>> 8+4*2-2*7
2
>>> 8+4*2-4/2
14.0
>>> 4--2
6
>>> 4-3.0
1.0
>>> 4    +    9
13
>>> 4+
SyntaxError: invalid syntax
>>> 23/4
5.75
>>> 23//4
5
>>> #lấy phần nguyên
>>> 23//4.2
5.0
>>> 23%4
3
>>> #lấy phần dư
>>> 23%4.2
1.9999999999999991
>>> 5*4.2+1.99999999991
22.99999999991
>>> 23///4.2
SyntaxError: invalid syntax
>>> 4**3
64
>>> #mũ 3
>>> 64**0.33333333
3.9999999445482257
>>> 64**.333334
4.000011090370264
>>> 4+(3**2)/2
8.5
>>> 4+3**2/2
8.5
>>> (4+3**2)/2
6.5
>>> #biến
>>> a=3
>>> a
3
>>> type(a)  #xác định kiểu của a
<class 'int'>
>>> Aa=4
>>> Aa*2
8
>>> b=4.1
>>> type(b)
<class 'float'>
>>> c=a+b
>>> c
7.1
>>> type(c)
<class 'float'>
>>> d=C*c-a**2-b**2
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    d=C*c-a**2-b**2
NameError: name 'C' is not defined
>>> d=c*c-a**2-b**2
>>> d
24.599999999999998
>>> #trong python có sự phân biệt in hoa và in thường
>>> a1=4
>>> _b=5
>>> c_=(a1-_b)**3
>>> c_-1
-2
>>> """
Để lưu trữ giá trị của biểu thức cuối cùng trong trình thông dịch.
Vì bỏ qua các giá trị cụ thể. (cái gọi là "Tôi không quan tâm")
Để cung cấp các ý nghĩa và chức năng đặc biệt cho tên của các vartiable hoặc các hàm.
Để sử dụng làm chức năng 'Quốc tế hóa (i18n)' hoặc 'Bản địa hóa (l10n)'.
Để tách các chữ số của giá trị chữ số
"""
'\nĐể lưu trữ giá trị của biểu thức cuối cùng trong trình thông dịch.\nVì bỏ qua các giá trị cụ thể. (cái gọi là "Tôi không quan tâm")\nĐể cung cấp các ý nghĩa và chức năng đặc biệt cho tên của các vartiable hoặc các hàm.\nĐể sử dụng làm chức năng \'Quốc tế hóa (i18n)\' hoặc \'Bản địa hóa (l10n)\'.\nĐể tách các chữ số của giá trị chữ số\n'
>>> n=6
>>> _m=8
>>> c_=(n-m)**2
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    c_=(n-m)**2
NameError: name 'm' is not defined
>>> c_=(n-_m)**2
>>> c_-1
3
>>> type(c)
<class 'float'>
>>> d,e=5.1,9
>>> d
5.1
>>> type(d)
<class 'float'>
>>> e
9
>>> type(e)
<class 'int'>
>>> d_e=d/e
>>> d_e
0.5666666666666667
>>> type(d_e)
<class 'float'>
>>> d1,e1=4.2,5.3
>>> d1,e1=e1,d1
>>> d1
5.3
>>> e1
4.2
>>> d1,e1=e1,d1-2
>>> d1
4.2
>>> e1
3.3
>>> d3,e3=d1*e1,d1/e2
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    d3,e3=d1*e1,d1/e2
NameError: name 'e2' is not defined
>>> d3,e3=d1*e1,d1/e1
>>> d3
13.86
>>> e3
1.272727272727273
>>> d2=e2=4.78
>>> d2
4.78
>>> e2
4.78
>>> d3+=1
>>> d3
14.86
>>> #d3=d3+1
>>> e3-=2
>>> e3
-0.7272727272727271
>>> d3/=2
>>> d3
7.43
>>> d3*=2
>>> d3
14.86
>>> d3*=e3
>>> d3
-10.807272727272723
>>> x,y=4.3,3
>>> z1,z2=y**x,y**int(x)
>>> z1
112.62152279558863
>>> z2
81
>>> float(y)
3.0
>>> z3,z4=float(y)**x,float(y)**int(x)
>>> z3
112.62152279558863
>>> z4
81.0
>>> int(4.7)
4
>>> 3*+4
12
>>> 12/-4
-3.0
>>> 12+5*8
52
>>> 60/5*3
36.0
>>> 60/5*3//2
18.0
>>> 4+-77/7
-7.0
>>> 4*5-77/11+7*2
27.0
>>> #logical operators
>>> a=22
>>> b=21
>>> a|b
23
>>> a&b
20
>>> a^b
3
>>> (~a)&(~b)
-24
>>> a<<2
88
>>> b>>2
5
>>> #nhị phân của số thập phân
>>> #string
>>> s1='great'
>>> type(s1)
<class 'str'>
>>> # '' hay "" như nhau .nhưng trong 1 số trường hợp đặc biệt chỉ  có thể dùng 1 loại
>>> s2='str'
>>> s3='day'
>>> s4=s1+s3
>>> s4
'greatday'
>>> s5=s1+ ' '+s3
>>> s5
'great day'
>>> s6=s5*3
>>> s6
'great daygreat daygreat day'
>>> # là số lần
>>> s6=s5+'!'
>>> s7=s6*3
>>> s7
'great day!great day!great day!'
>>> print(s1)
great
>>> a=35
>>> print(a)
35
>>> a,b,c=10,21.3,True
>>> print(a,b,c)
10 21.3 True
>>> c=a*b
>>> b=11
>>> c=a*b
>>> repr(c)
'110'
>>> #repr in đối tượng đầu vào
>>> type(repr(c))
<class 'str'>
>>> print('product of a and b is'+'='+repr(c))
product of a and b is=110
>>> 0.2 + 2.3 – 9.7 + 11.2
SyntaxError: invalid character in identifier
>>> 0.2+2.3_9.7+11.2
SyntaxError: invalid syntax
>>> 0.2+2.3-9.7+11.2
4.0
>>>  4.2 - 2.3 + 9.7 - 11.2
 
SyntaxError: unexpected indent
>>> 4.2-2.3+9.7-11.2
0.40000000000000036
>>> 97%3
1
>>> pow(97,3,23)
10
>>> pow(3,97,23)
18
>>> 