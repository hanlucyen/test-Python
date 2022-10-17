#tạo một hàm sắp xếp
"""
def thuTu():
    i=input()
    j=input()
    k=input()
    l=input()
    m=input()
    n=input()
    list_my=[i,j,k,l,m,n]
    list_new=sorted(list_my)
    return list_new
print(thuTu()
"""

def check_order_list(mylist):
    print(sorted(mylist))
    return "hi"
h=[2,3,4,5,1,8,7,9]
print(check_order_list(h))

#tạo 1 hàm không trùng
def check_duplicate_list(mylist):
    if len(mylist)!=len(set(mylist)):
        return "tồn tại phần tử trùng lặp trong list!"
    else:
        return "không có phần tử trùng lặp trong list!"
i=[0,2,2,3,1,2,3,2]
print(check_duplicate_list(i))

