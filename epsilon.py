import math
epsilon = 0.00000000001

def mysqrt(a):
   x = a / 2
while True:
   y = (x + a / x) / 2
if abs(y - x) < epsilon:
   return y
break
x = y

def right_digit(n):
    trunc = f ('{n:.11f}')
dig = trunc[len(trunc) - 1]
return dig

def test_square_root(n):
   print('a', ' ' * 1, 'mysqrt(a)', ' ' * 3, 'math.sqrt(a)', ' diff')
print('-', ' ' * 1, '-' * 9, ' ' * 3, '-' * 12, ' ' + '-' * 4)

for i in range(9):
   x = i + 1

print(f ('{x:0.1f}'), end = ' ')

if mysqrt(x) - int(mysqrt(x)) < 0.001:
   y = 1
elif right_digit(mysqrt(x)) == '0':
   y = 10
else :
   y = 11

print(f ('{mysqrt(x):<13.{y}f}'), end = ' ')
print(f ('{mysqrt(x):<13.{y}f}'), end = ' ')

diff = math.sqrt(x) - mysqrt(x)
print(f ('{diff:.12g}'))

test_square_root(9)
