# def sum(x,y):
#     return x+y

# def mylt(x,y):
#     return x*y

# def calc(op, a, b):     # Воспиринимаем "op" принимаем как отдельную функцию.
#     print(op(a, b))     #  в качестве аргумента может быть целая функция.
#     # return op(a, b)

# calc(mylt, 4, 5)
# # ---------------------------------
#  #    АНАНОМНАЯ ФУНКЦИЯ LAMBDA

# sum = lambda x,y: x+y    # Анонимная функция
# print(sum(4,5))
# calc(lambda x,y: x+y+1, 4, 5)     # Тоже самое, создали функцию в вызове, тем самым сократили
# # -------------------------------------------------
# #       List Comprehension
# list = []

# for i in range(1, 101): #Создали функцию выведения четных чисел в список
#     if (i%2 == 0):
#         list.append(i)
# print(list)

# #   Аналогичное создание функции
# list = [i for i in range(1,21) if i%2 == 0]   #Аналогичное создание функции
# print(list)

# #  Создание пар кортежей
# list = [(i,i) for i in range(1,21) if i%2 == 0]   #Создание пар кортежей
# print(list)

# # создаем функцию и добавляем ее в условие, далее еще добавим кортеж
# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1,21) if i%2 == 0]
# print(list)

# list2 = [1,2,3,5,8,15,23,38]

# def squad(x):
#     return x**2
# listnew = [(i, squad(i)) for i in list2 if i%2 ==0]
# print(listnew)

# ----------------------------------------
# #          Функция Map()
# li = [x for x in range(1,20)]
# li = list(map(lambda x: x+10, li))      #чтоб получить набор данных, нам требуется превратить его в список, преобразуем с помощью list

# print(li)
# -----------------
data = list(map(int,'1 2 34'.split()))

for e in data:
    print(e*10)
# --------------------------------
##       Функция FILTER()
data = [x for x in range(10)]

res = list(filter(lambda x: not x%2, data))  # the same x%2 == 0 
print(res)

# ------------------------------
## Функция ZIP()
user = ['user1', 'user2', 'user3', 'user4']  # Есть набор данных юзеров
ids = [4,5,7,10]  # есть набор индексов
salary = [111, 222, 44]

data= list((user, ids, salary)) # выполняем ф-ию zip(), ложем результат в data
print(data)
## ФУНКЦИЯ ENUMERATE()
#  Позволяет передать на вход набор данных, а на выход получаете кортежи с пронумерованными элементами( только 1 набор данных)
data= list(enumerate(user))
print(data)