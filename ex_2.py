a, b = map(int, input('Введите размер отверстия через x: ').split('x'))
c, d, e = map(int, input('Введите размер кирпичей через x: ').split('x'))
s_rectangle = a * b
s_parallelepiped_1 = d * e
s_parallelepiped_2 = c * d
if s_rectangle >= s_parallelepiped_1 or s_rectangle >= s_parallelepiped_2:
    print('да')
else:
    print('нет')
