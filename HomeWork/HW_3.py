# №1      Задайте список из нескольких чисел. Напишите программу,
#   которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
# size = int(input('Enter size of array: '))
# list = []
# for i in range(size):
#     list.append(random.randint(1, 30))
# print(list)

# sum = 0
# for i in range(1,len(list),2):
#     sum += list[i]
# print(sum)

# ---------------------------------------------
#  №2  Напишите программу, которая найдёт произведение пар чисел списка. 
#       Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

size = int(input('Enter size of array: '))
list = []
new=[]
for i in range(size):
    list.append(random.randint(1, 10))
print(list)

for i in range(int(len(list)/2+1)):
    if i== 0:
        new.append(list[0]*list[-1])
    else:
        new.append(list[-i-1]*list[i])
print(new)        
    