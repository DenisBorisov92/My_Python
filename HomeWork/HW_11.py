# Jupyter Notebook и несколько слов об аналитике

#  Дана функция

#  f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30




import numpy as np
import matplotlib.pyplot as plt

color = 'g'
x_limit = [-2, 2.2]
koef = [-12, -18, 5, 10, -30]

def func(x, a, b, c, d, e):
    return a * x**4 * np.sin(np.cos(x)) + b * x**3 + c * x**2 + d * x - e

x = np.arange(x_limit[0], x_limit[1], 0.01)

change_x = []
change_dir = 1

for i in range(len(x) - 1):
    if change_dir == -1:
        if func(x[i], *koef) < func(x[i+1], *koef):
            change_x.append((x[i], func(x[i], *koef)))
            change_dir = 1
    else:
        if func(x[i], *koef) > func(x[i+1], *koef):
            change_x.append((x[i], func(x[i], *koef)))
            change_dir = -1

def change_color():
    global color
    if color == 'g':
        color = 'b'
    else:
        color = 'g'
    return color

plt.figure(figsize=(15, 5))
current_x = np.arange(x_limit[0], change_x[0][0], 0.01)
plt.plot(current_x, func(current_x, *koef), change_color())

for i in range(len(change_x) - 1):
    current_x = np.arange(change_x[i][0], change_x[i+1][0], 0.01)
    plt.plot(current_x, func(current_x, *koef), change_color())

current_x = np.arange(change_x[-1][0], x_limit[1], 0.01)
plt.plot(current_x, func(current_x, *koef), change_color())

plt.title("График функции")
plt.grid()
plt.show()