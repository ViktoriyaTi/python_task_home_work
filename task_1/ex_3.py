# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример: x=34; y=-30 -> 4, x=2; y=4-> 1,	x=-34; y=-30 -> 3

print('Введите значение координаты Х = ')
X = int(input())
print('Введите значение координаты Y = ')
Y = int(input())
if X == 0 and Y == 0:
    print('Точка с координатами Х = 0, Y = 0 представляет начало координат')
elif (X > 0 or X < 0) and Y == 0:
    print (f'Точка с координатами Х = {X} , Y = {Y} лежит на оси Х')  
elif (Y > 0 or Y < 0) and X == 0:
    print (f'Точка с координатами Х = {X} , Y = {Y} лежит на оси Y')  
elif X > 0 and Y > 0:
    print (f'Точка с координатами Х = {X} , Y = {Y} лежит в 1 четверти')
elif X < 0 and Y > 0:
    print (f'Точка с координатами Х = {X} , Y = {Y} лежит в 2 четверти')
elif X < 0 and Y < 0:
    print (f'Точка с координатами Х = {X} , Y = {Y} лежит в 3 четверти')
else:
    print (f'Точка с координатами Х = {X} , Y = {Y} лежит в 4 четверти')
    