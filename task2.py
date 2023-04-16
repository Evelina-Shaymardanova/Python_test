# Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# a = input("Введите трехзначное число:")
# if len(a) == 3:
#     b = int(a)
#     print(b // 100 + b // 10 % 10 + b % 10)
# else:
#     print("Ошибка")


my_dic = {}
m_dirw = {}
m_dirw["names"] = "Evelina"
my_dic["name"] = "Dinar"
my_dic["Age"] = "33"
my_dic["Age"] = "55"
my_dic.update(name = "DINAR")
my_dic.update(m_dirw)

print("Age" in my_dic)
print(my_dic.items())
print(my_dic.keys())
print(my_dic.values())
print(my_dic["Age"])
print(len(my_dic))
print(my_dic)