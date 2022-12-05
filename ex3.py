# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19
lst = [1.1, 1.2, 3.1, 10.01]
new_lst = []


for i in range(len(lst)):
    strr = str(lst[i])
    spl = strr.split('.')
    num = spl[1]
    new_lst.append(num)
    # print(new_lst)

new_lst_mult = []
for i in range(len(new_lst)):
    mult_num = int(new_lst[i]) * 100
    new_lst_mult.append(mult_num)

# divide()
print(new_lst_mult)
