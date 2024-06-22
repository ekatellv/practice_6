import math

a, b = map(float, input('Введите размер через x: ').split('x'))
r = 6.5
s_carpet = a * b
d_carpet = math.sqrt(a ** 2 + b ** 2)
if d_carpet <= 2 * r:
    print('да')
else:
    print('нет')
