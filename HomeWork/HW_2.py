#   №1  Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.

# n = input('Введите любое вещественное число: ')
# sum = 0

# for i in range(len(n)):
#     if n[i].isdigit():
#         sum += int(n[i])

# print(sum)

#   №2. Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Enter any integer: '))
# list = []
# num = 1
# for i in range(1, N+1):
#     num *= i
#     list.append(num)

# print(f'пусть N = {N}, тогда {list}')

#  №3   Задайте список из n чисел последовательности (1+1/n)n и 
# выведите на экран их сумму
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} 
# Сумма 9.06

# n = int(input('Enter any integer: '))
# d = {i:round(((1+1/i)**i),2) for i in range(1, n+1)}
# print(f'Для n={n} {d}')

# # print(d.keys())
# # print(d.values())
# sum = 0
# t = list(d.values())
# for i in range(len(t)):
#     sum += t[i]
# print(round(sum,2))

#  №4  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint
N = int(input('Enter size of array: '))
arr= list(range(-N,N+1))
print(arr)

f = open('file.txt', 'r')
s=0
for line in f:
    s+=int(line)
    print(s)
f.close()
#В данной задаче не получается обратится к каждой строчке файла к индексу, чтоб взять от туда число

# №5  Реализуйте алгоритм перемешивания списка.
# import random
# size = int(input('Enter size of array: '))
# list = []
# for i in range(size):
#     list.append(random.randint(-10, 20))
# print(list)

# random.shuffle(list)
# print(list)