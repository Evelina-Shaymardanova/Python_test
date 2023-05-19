# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
#
# total = 0
# for row in my_list:         # в один цикл
#     total += sum(row)
#     print(total)

# a = 5
# for i in range(5):
#     print(" " * (5 - i), 5)

# s = list("Марка вина \\Ягодка\\")
# s.insert(2, True)
# s.remove("\\")
# s.remove("\\")
# del s[2]
# print(s)

# ________________Генерирует вложенный список_____________________
# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [0] * n
#
# n = 4                                          # количество строк (элементов)
# my_list = []
#
# for _ in range(n):
#     elem = [int(i) for i in input().split()]   # создаем список из элементов строки
#     my_list.append(elem)
# print(my_list)

# list(i for i in input())

# ________________Выпрямляет вложенный список_____________________
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
# sum(my_list, [])
# >>>[1, 9, 8, 7, 4, 7, 3, 4, 2, 1]
# print(sum(my_list, []))
# >>>46

# s = list(input("Введите строку: "))
# s1 = [[]]
#
# for i in s:
#     s1.append([i])
# for i in s1:
#     for j in i:
#         s1[i][j] = s1[i][j + 1]
#         if j == i:
#             s1.append(j)
# print(s1)


# ________________ТРЕУГОЛЬНИК ПАСКАЛЯ!!!!_____________________
# n = int(input("Введие число для треугольника Паскаля: "))
# res = [1]
# for k in range(n):
#     print(" " * (n-k), *res)
#     res = [1] + [res[i] + res[i+1] for i in range(k)] + [1]

# f = [123]
# f += [2]    # [2] - обозначает элемент, а не индекс
# print(f)

# print(matrix, sep = "\n")

# ________________Нахождение большего элемента в массиве по главной диагонали матрицы!!!!_____________________
# n = int(input("Введите количество строк в матрице: "))
# matrix = []
#
# for i in range(n):
#     st = [int(i) for i in input().split()]
#     matrix.append(st)
# print(matrix)
#
# s_max = matrix[0][0]
# for i in range(n):
#     for j in range(n):
#         if i >= j and matrix[i][j] > s_max:
#             s_max = matrix[i][j]
# print(s_max)


