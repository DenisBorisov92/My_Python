#Задача №1 Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#          и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# int = int(input('Input the number day of week: '))
# if int <=7 and int > 5:
#     print (f'Yes, {int} day is day-off')
# elif int >=1 and int <=5:
#     print(f'No, {int} day is not day-off')
# else:
#     print(f"you didn't input correct number")

# -----------------------------------------------------------------
#     Задача №3
# Напишите программу, которая принимает на вход координаты точки (X и Y), п
# ричём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1

# X = float(input('Enter coordinate x: '))
# Y = float(input('Enter coordinate y: '))
# if X > 0 and Y > 0:
#     print('it is I quarter')
# if X < 0 and Y > 0:
#     print('it is II quarter')
# if X < 0 and Y > 0:
#     print('it is III quarter')
# if X > 0 and Y < 0:
#     print('it is IV quarter')
# else:
#     print('it is not correct coordinate')

#     Задача №4
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = input('Enter number of quater (from 1 to 4): ')
# if quarter == 1:
#     print('Х > 0 and Y > 0.')
# elif quarter == 2:
#     print('Х < 0 and Y > 0.')
# elif quarter == 3:
#     print('Х < 0 and Y < 0.')
# elif quarter == 4:
#     print('Х > 0 and Y < 0.')
# else:
#     print('Warning. It is not number of quarter')

#     Задача №5
# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

Xa = float(input('Enter coordinate x of point A: '))
Ya = float(input('Enter coordinate y of point A: '))
Xb = float(input('Enter coordinate x of point B: '))
Yb = float(input('Enter coordinate y of point B: '))
distance = (((Xb - Xa)*2)+((Yb-Ya)*2))**0.5
print(f'Distance between points A and B is {distance:.2f}')