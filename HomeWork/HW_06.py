# №1      Задайте список из нескольких чисел. Напишите программу,
#   которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

size = int(input('Enter size of array: '))
li=[random.randint(1,14) for i in range(size)]
print (li)

res = [li[i] for i in range(1,len(li),2)]
print(res)
print(sum(res))

# def Summa():
#     for i in range(1,len(li),2):
#         sum=0
#         sum += li[i]
#         return sum
# print(Summa())
    # Почему не получилдось через функцию? Создав ее, она выдает только одно значение, а не сумму, я хотел при помоща нее прогнать через Ф-ию Map



#  №2  Напишите программу, которая найдёт произведение пар чисел списка.
#       Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

size = int(input('Enter size of array: '))

spisok = [random .randint(1,10) for i in range(size)]
print(spisok)
new = [spisok[-i-1]*spisok[i] for i in range(int(len(spisok)/2+len(spisok)%2))]
print(new)