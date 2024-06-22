chess = input('Введите название клетки: ')
if chess[0] in ('a,c,e,g') and int(chess[1]) % 2 == 0:
    print('белый')
elif chess[0] in ('a,c,e,g') and int(chess[1]) % 2 != 0:
    print('черный')
elif chess[0] in ('b,d,f,h') and int(chess[1]) % 2 == 0:
    print('черный')
else:
    print('белый')
