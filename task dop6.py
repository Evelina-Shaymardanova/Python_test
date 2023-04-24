# 6. Дана строка ( возможно, пустая), состоящая из букв A-Z
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.


def rle(input_str: str) -> str:
    if not input_str.isalpha():
        return "невалидная строка"
    temp = input_str[0]
    temp_count = 1
    t = []
    for i in range(1, len(input_str)):
        if temp == input_str[i]:
            temp_count += 1
        else:
            t.append((temp, temp_count))
            temp = input_str[i]
            temp_count = 1
    t.append((temp, temp_count))
    rez_str = ""
    for elem in t:
        if elem[1] > 1:
            rez_str += elem[0]
            rez_str += str(elem[1])
        else:
            rez_str += elem[0]
    return rez_str


print(rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'))
print(rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBB5286BBBBBBBBBBBBBBBBBBB'))
print(rle(''))