# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), 
# применив лямбды, filter, map, zip, enumerate, списочные выражения.

    # Задача ДЗ_task_3_ex_3
    # Задайте список из вещественных чисел. 
    # Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
    # Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = list(map(float, input('Введите список из вещественных чисел через пробел: ').split()))
lst2 = [i - int(i) for i in lst]
print(round(max(lst2)-min(lst2),3))


    #  Задача Семинар_5_задание_1
    # В файле находится N натуральных чисел, записанных через пробел.
    # Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
    # 1 2 3 5 6 7 8
    # выходные 4


with open('1.txt', 'r', encoding = 'utf8') as data:
    lst = data.readline().split()
lst = [int(i) for i in lst]    
lst = [i for i in range(1, len(lst)) if lst [i]-1 != lst[i-1]]
lst1 = list(map(lambda x: x + 1, lst))
print(lst1)


