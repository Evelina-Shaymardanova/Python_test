s = int(input("Введите сумму: "))
p = int(input("Введите произведение: "))
for x in range(1, 1001):
    for y in range(x):
        if x+y == s and x*y == p:
            print(x, y)
