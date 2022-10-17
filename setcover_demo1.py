import sys, itertools
from pulp import *

noidung_tap = [ ['1','3','4', '6', '7'],
                           ['4', '7', '8', '12'],
                           ['2', '5', '9', '11', '13'],
                           ['1', '2', '18', '19', '21'],
                           ['3','6','10', '12', '14'],
                           ['8', '14', '15', '16', '17'],
                           ['18', '21', '24', '25'],
                           ['2','10','16','23'],
                           ['1','6','11'],
                           ['20','22','24','25'],
                           ['2','4', '6','8'],
                           ['1', '6', '12', '17']
                ]

taphop = range( len(noidung_tap))
cac_phantu = set(itertools.chain(*noidung_tap))
model = LpProblem('Setcover', LpMinimize)
chon = LpVariable.dicts('Tap_chon', taphop, 0, 1, LpInteger)
model += lpSum(chon), "Cac tap duoc chon"

for j in cac_phantu:
	model += lpSum(chon[i] for i in taphop if j in noidung_tap[i]) >=1, "Phan tu %s" %j

model.solve()

for i in taphop:
	if chon[i].value() == 1:
		print (noidung_tap[i], " là các camera thứ " + str(i+1))
