#   Задача №1

# a = int(input('Input number a: '))
# b = int(input('Input number b: '))
# if a == b*b:
#     print('integer b is square of integer a')
# elif b == a*a:
#     print('integer b is square of integer a')
# else:
#     print('Not')


#  Задача №2
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90
# max = int(input(f' Input 1 numbers: '))
# for i in range(4):
#     i += 1
#     num = int(input(f' Input {i+1} numbers: '))
#     if num > max:
#         max = num
# print(max)


#  Задача №3. Работа в группах

#  Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
#         Мой способ
# # num = int(input('Input number: '))
# # ran = range (-num, num+1)
# # numbers = list(ran)
# # print(numbers)
# # -----------------------------
#          2способ
# # N = int(input('Input numbers N: '))
# # N = abs(N)

# # for i  in range(-N, N):
# #     print(i, end =', ')
# # print(N)
#          3 способ
# N = int(input('Input numbers N: '))
# num = -N
# while num <= N:
#     print(num, end=', ')
#     num+=1
    

    # Задача №4. Работа в группах
# Напишите программу, которая будет принимать на вход дробь и показывать 
# первую цифру дробной части числа.
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

# N = float(input('Введите число N: '))
# if N % 1 == 0:
#     print("нет")
# else:
#     N *= 10
#     N = int(N % 10)
#     print(N)

# Задача №5. Работа в группах
# Напишите программу, которая принимает на вход число и проверяет, 
# кратно ли оно 5 и 10 или 15, но не на 30


# N = int(input('Input number N: '))
# if (N%5 == 0 and N%10 == 0 or N%15 == 0) and N%30!=0:
#     print('true')
# else:
#     print('no')

# # ------------------------
# # Пример решения с помощью функции

# def multiple(num):
#     if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
#         print("Число удовлетворяет данным условиям")
#     else:
#         print("Число не удовлетворяет данным условиям")

# num = int(input("Введите число: "))
# multiple(num)


#  Задача для числа Фибонначи
N = int(input('Input number N: '))
F = 1
num = 1
while num <= N:
    F=F*num
    num +=1
print(F)

# N = int(input('Input number N: '))
# F = 1
# for i in range(1,N+1):
#     F=F*i
# print(F)

# Два разных решения