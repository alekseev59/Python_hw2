# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random

count = 0
num = int(input('Задайте кол-во чисел в массиве: '))

list = [random.randint(-100, 100) for i in range(num)]
for i in range(num):
    if list[i] < 0:
        list.insert(i+1, count)
    if list[-1] < 0:
        list.append(0)
print(list)
