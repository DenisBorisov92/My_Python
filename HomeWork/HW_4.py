#   №1Вычислить число c заданной точностью d
#   при d = 0.001, π = 3.141.  10^-1 ≤ d ≤10^-10

# import math
# from re import I
# result = input('Введите точность в диапазоне от 0.1 до 0.0000000001: ')
# punctuality = len((result).replace('0.', ''))
# print(f'Число Пи с заданной точностью знаков после запятой ({punctuality}): {math.pi:.{punctuality}f}')

# --------------------------
# 2.    Задайте натуральное число N. Напишите программу, 
#   которая составит список простых множителей числа N.

N = int(input('Enter any integer: '))
list=[]
i=2
while i <= N:
    if N%i==0:
        list.append(i)
        N//= i
    else:
        i+=1
print(f'Список простых множителей числа {N} - {list}')

