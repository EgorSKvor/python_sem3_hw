# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
lst = [2, 3, 4, 5, 6]
new_lst = []

# def find_len_mas():
#     count = False
#     if len(lst) % 2 == 0:
#         count = True
#     else:
#         count = False
#     return count


def find_mult_odd():
    count = 0
    count_rev = -1
    for i in range((len(lst) + 1)//2):
        mult = lst[count]*lst[count_rev]
        count += 1
        count_rev -= 1
        new_lst.append(mult)
    print(new_lst)


find_mult_odd()
