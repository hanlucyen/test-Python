LTGIS = ['CNTT', 'GIS', 'Python', '45tiet', 'SV.Lieu','SV.Hoa','SV.Mai', 'SV.Giang']
SV = ['SV.Lieu', 'SV.Mai', 'SV.Giang']
Phanmem = ['ArcGIS', 'MapInfo', 'gvSIG', 'QGIS', 'GeoServer']
Lop = [SV, Phanmem, 'Maytinh']
ngaylamviec = ['Thu 2', 'Thu 3', 'Thu 4', 'Thu 5', 'Thu 6']
cuoituan = ['Thu 7', 'Chu nhat']
print(LTGIS)
print(LTGIS[0])
print(LTGIS.reverse())
print(LTGIS)
print(Phanmem.append('ArcGIS Server'))
print(len(Phanmem))
print(Phanmem.sort())
print(Phanmem)
thutrongtuan=ngaylamviec+cuoituan
print(thutrongtuan)
print(thutrongtuan.count('Thu3'))
print(SV.insert(1,'SV.Hoa'))
print(SV)
print(SV.pop())
print(SV.sort())
print(SV.remove('SV.Mai'))
print(SV)

      



