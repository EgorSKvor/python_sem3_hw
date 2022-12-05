# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# num = int(input('Enter num '))
# fib1 = fib2 = 1
# fib_lst_pos = []
# fib_lst_neg = []
# for i in range(2, num):
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     fib_lst_pos.append(fib2)
# fib1_neg = fib2_neg = 1
# for i in range(2, num):
#     fib_summ = fib1_neg + fib2_neg
#     fib1_neg = fib2_neg
#     fib2_neg = fib_summ
#     fib_lst_neg.append(fib2_neg)
# fib_lst_neg_new = []
# for i in range(len(fib_lst_neg)):
#     if fib_lst_neg[i % 2 == 0]:
#         fib_lst_neg_new.append(fib_lst_neg[i])
#     else:
#         fib_lst_neg_new.append(fib_lst_neg[i]*(-1))


# res = fib_lst_neg_new + fib_lst_pos
# print(fib_lst_neg_new)


# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)


def reversed_fibonacci(n):
    if n in (1, 2):
        return 1
    return reversed_fibonacci(n + 2) - reversed_fibonacci(n + 1)


def negafibonacci() -> list:
    a = []
    b = []
    try:
        n = int(input("Введите число для последовательности Фибоначчи:"))
        if type(n) in [int]:
            for i in range(-n, n + 1):
                if i > 0:
                    a.append((fibonacci(i)))
                else:
                    b.append(reversed_fibonacci(i))
            return f'- для k={n} список будет выглядеть так: {b + a}'
    except ValueError as e:
        print(e)
        return negafibonacci()


print(negafibonacci())


def fibonacci(number: int):
    inner_list: list[int] = []
    for item in range(number+1):
        match item:
            case 0 | 1:
                inner_list.append(item)
            case _:
                inner_list.append(inner_list[item-2]+inner_list[item-1])
    return inner_list
