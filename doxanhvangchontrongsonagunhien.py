from _future_ import division
import numpy as np
import random,pdb
import operetor
def cnkd(trongso):
    trongso_chiso_sxep=sorted(enumerate(trongso),key=operator.itemgetter(1))
    chiso,trongso_sxep=zip(*trongso_chiso_sxep)
    tong=sum(trongso_sxep)
    print('tong',tong)
    xac_suat=[x/tong for x in trongso_sxep]
    print('xac suat tich luy=',xs_tichluy)
    print('chi so tuong ung=',xs_tichluy)
    so_ngau_nhien=random.random()
    print('so ngau nhien=',so_ngau_nhien)
    for chi_so,giatri_tichluy_xs in zip(chiso,xs_tichluy):
        if so_ngau_nhien<giatri_tichluy_xs:
            return chi_so



bo_trongso=[87,3,20]
cnkd(bo_trongso)
for i in range(20):
    cnkd(bo_trongso)
for i in range(30):
    cnkd(bo_trongso)
bo_trongso=[20,10,70]
