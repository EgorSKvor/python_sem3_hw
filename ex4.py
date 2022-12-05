# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Enter num --> '))
double_num = str
while num != 0:
    double_num = num % 2
    num = num // 2
    print(double_num, end="")
