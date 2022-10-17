x = int(input("Nhap mot so: "))
if x < 0:
   x = 0
   print('So am')
elif x == 0:
   print('So 0')
elif x == 1:
   print('So 1')
else:
   print('So duong')
nhiet_do= int(input("Nhap mot so: "))
def kiemtra_nuocsoi(nhietdo):
	if nhiet_do<100:
		return "Nuoc chua soi!"
	else:
		return"Nuoc da soi!"

nhiet_do= int(input("Nhap mot so: "))
def kiemtra_nuocsoi(nhietdo):
	if nhiet_do<100:	
		print("chua soi")
	else:
                print("da soi")
