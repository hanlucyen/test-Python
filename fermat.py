import math
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
n=int(input("n: "))
if a^n+b^n==c^n:
    n>2
    print("Fermat đã sai!")
else:
    print("Fermat vẫn đúng!")
