# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

mx = int(input("Введите максимум диапазона: "))
mn = int(input("Введите минимум диапазона: "))
ms = []
ms1 = []
rm = int(input("Введите размер списка: "))

import random
for i in range(0, rm + 1):
    n = random.randint(-100, 100)
    ms.append(n)
print(ms)

for j in range(len(ms)):
    if mn <= ms[j] <= mx:
        ms1.append(j)
print(ms1)