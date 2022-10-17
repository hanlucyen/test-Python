import itertools
itertools.cycle('ABC')
taphop=itertools.cycle('ABC')
soluong_max=20
phantu_dang_xemxet=0
for phantu in taphop:
	if phantu_dang_xemxet>=soluong_max:
            break
        else:
            print(phantu)
            phantu_dang_xemxet=phantu_dang_xemxet+1
            
        
		
exit()
#to hop
 for i in itertools.product('AB','CD','EFIGK'):
	print(i)
