# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите количество обрабатываемых чисел = '))
sum = 0
for i in range(1,n+1):
    a = (1+1/i)**i
    sum = sum + a
print(round(sum,3))