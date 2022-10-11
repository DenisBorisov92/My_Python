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

X = float(input('Enter coordinate x: '))
Y = float(input('Enter coordinate y: '))
if X > 0 and Y > 0:
    print('it is I quarter')
if X < 0 and Y > 0:
    print('it is II quarter')
if X < 0 and Y > 0:
    print('it is III quarter')
if X > 0 and Y < 0:
    print('it is IV quarter')
else:
    print('it is not correct coordinate')
