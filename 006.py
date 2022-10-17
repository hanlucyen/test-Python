Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def bool_xy(x,y):
	kq=0
	if (x==1) and (y==1):
		kq=0
	if (x==1) and (y==0):
		kq=1
	if (x==0) and (y==1):
		kq=0
	if (x==0) and (y==1):
		kq=0
	return kq

>>> for x in [1,0]:
	for y in [1,0]:
		print(bool_xy(x,y))

		
0
1
0
0
>>> def bool_xy1(x,y):
	kq=0
	if (x==1) and (y==0):
		kq=1
	return kq

>>> for x in [1,0]:
	for y in [1,0]:
		print(bool_xy1(x,y))

		
0
1
0
0
>>> trang_thai="s0"
>>> def chuyen(tin_hieu):
	global trang_thai
	if trang_thai=="s0":
		if tin_hieu==0:
			print("0-s0")
		elif tin_hieu==1:
			print("1-s1")
			trang_thai="s1"
	elif trang_thai=="s1":
		if tin_hieu==0:
			print("0-s1")
			trang_thai="s1"
		elif tin_hieu==1:
			print("1-s2")
			trang_thai="s2"
	elif trang_thai=="s2":
		if tin_hieu==0:
			print("0-s2")
			trang_thai="s2"
		elif tin_hieu==1:
			print("1-s0")
			trang_thai="s0")
			
SyntaxError: unmatched ')'
>>> def chuyen(tin_hieu):
	global trang_thai
	if trang_thai=="s0":
		if tin_hieu==0:
			print("0-s0")
		elif tin_hieu==1:
			print("1-s1")
			trang_thai="s1"
	elif trang_thai=="s1":
		if tin_hieu==0:
			print("0-s1")
			trang_thai="s1"
		elif tin_hieu==1:
			print("1-s2")
			trang_thai="s2"
	elif trang_thai=="s2":
		if tin_hieu==0:
			print("0-s2")
			trang_thai="s2"
		elif tin_hieu==1:
			print("1-s0")
			trang_thai="s0"

			
>>> tap_tinhieu=[1,0,1,0,1,1,0,0,1]
>>> for i in tap_tin:
	chuyen(i)

	
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    for i in tap_tin:
NameError: name 'tap_tin' is not defined
>>> for i in tap_tinhieu:
	chuyen(i)

	
1-s1
0-s1
1-s2
0-s2
1-s0
1-s1
0-s1
0-s1
1-s2
>>> trang_thai="s0"
>>> trangthai_ke={'s0':['s0','s1'],
	      's1':['s1','s2'],
	      's2':['s2','s0']}
>>> ket_qua={'s0':[0,1],
	 's1':[0,1],
	 's2':[0,1]}
>>> def chuyen_trangthai(tin_hieu):
	global trang_thai
	chuoi_in=str(ket_qua[trang_thai][tin_hieu])
	chuoi_in=chuoi_in+" - "+trangthai_ke[trang_thai][tin_hieu]
	print(chuoi_in)
	trang_thai=trangthai_ke[trang_thai][tin_hieu]

	
>>> tap_tinhieu=[1,0,1,0,1,1,0,0,1]
>>> for i in tap_tinhieu:
	chuyen_trangthai(i)

	
1 - s1
0 - s1
1 - s2
0 - s2
1 - s0
1 - s1
0 - s1
0 - s1
1 - s2
>>> class StateMachie:
	def _init_(self):
		self.tap_xuly={}
		self.trangthaiBatdau= None
		self.trangthaiKetthuc=[]
	def them_Trangthai(self,trangthai,xuly,trangthai_ketthuc=0):
		trangthai=trangthai.upper()
		self.tap_xuly[trangthai]=xuly
		if trangthai_ketthuc:
			self.trangthaiKetthuc.append(trangthai)
	def thietlap_TrangthaiBatdau(self,trangthai):
		self.trangthaiBatdau=trangthai.upper()

		
>>> class StateMachie:
	def _init_(self):
		self.tap_xuly={}
		self.trangthaiBatdau= None
		self.trangthaiKetthuc=[]
	def them_Trangthai(self,trangthai,xuly,trangthai_ketthuc=0):
		trangthai=trangthai.upper()
		self.tap_xuly[trangthai]=xuly
		if trangthai_ketthuc:
			self.trangthaiKetthuc.append(trangthai)
	def thietlap_TrangthaiBatdau(self,trangthai):
		self.trangthaiBatdau=trangthai.upper()
	def thucthi(self,dauvao):
		try:
			xuly=self.tap_xuly[self.trangthaiBatdau]
		except:
			raise InitializationError("phai gfi .thietlap_TrangthaiBatdau() truoc khi goi .thucthi() ")
		if not self.trangthaiKetthuc:
			raise InitializationError("it nhat 1 trang thai phai la trang thai ket thuc")
		while True:
			(TrangThaiMoi,dauvao)=xuly(dauvao)
			if TrangThaiMoi.upper() in self.trangthaiKetThuc:
				print("den dich!",TrangThaiMoi)
				break
			else:
				xuly=self.tap_xuly[TrangThaiMoi.upper()]

				
>>> from statemachine import StateMachine
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    from statemachine import StateMachine
ModuleNotFoundError: No module named 'statemachine'
>>> from statemachine import StateMachine
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    from statemachine import StateMachine
ModuleNotFoundError: No module named 'statemachine'
>>> from statemachine import StateMachine
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    from statemachine import StateMachine
ModuleNotFoundError: No module named 'statemachine'
>>> from statemachine import StateMachine
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    from statemachine import StateMachine
ModuleNotFoundError: No module named 'statemachine'
>>> 
================ RESTART: C:/Users/ASUS/Documents/ctrr/statest.py ===============
Traceback (most recent call last):
  File "C:/Users/ASUS/Documents/ctrr/statest.py", line 1, in <module>
    from statemachine import StateMachine
ImportError: cannot import name 'StateMachine' from 'statemachine' (C:/Users/ASUS/Documents/ctrr\statemachine.py)
>>> 