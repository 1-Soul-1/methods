# Типы интегралов
"""
Одномерный(quad)
Двумерный(dquad) - функция, которая сначала принимает Х, а потом Y(обратный порядок)
Тройной(tquad) - сначала Z, а потом Y и X
N-мерный(nquad)
"""

from scipy.integrate import quad, dblquad, tplquad, nquad
import numpy as np

# Одномерный интеграл
def f(x):
    return x**2

result, error = quad(f,0,2)
print(f"∫x2dx от 0 до 2 = {result}")
print(f"Погрешность: {error}")



# Двумерный интеграл
def dbf(x,y):
    return x*y

result, error = dblquad(dbf,0,2,0,2)
print(f"∬x*y dxdy = {result}")



# Тройной интеграл
def tpf(x,y,z):
    return x*y*z

result, error = tplquad(tpf,0,2,0,3,0,2)
print(f"∭x*y*z dxdydz = {result}")



# Многомерный интеграл
def nf(x1,x2,x3,x4):
    return x1+x2+x3+x4

# Находим пределы для каждого Х
range = [(0,2),(0,2),(0,2),(0,2)]
result, error = nquad(nf, range)
print(result)


# Задание 1:
# Вычислить площадь под кривой
# Парабола y = x² на отрезке [0, 2]
# Прямая y = 2x на отрезке [0, 2]
# Константа y = 5 на отрезке [0, 2]
# Синус y = sin(x) на отрезке [0, π]
print("Задание 1")
def task1_func(x):
    return 3*x**2+2*x

result, error = quad(task1_func, 0,3)
print(f"∫(3x²+y²) dxdy от 0 до 3 = {result}")
print(f"Погрешность: {error}")


# Задание 2:
# Скорость машины меняется по закону v(t) = t² + 2t + 1 (м/с).
# Какой путь проедет машина за 3 секунды?
# Какой путь проедет машина с 1-й по 3-ю секунду?
print("Задание 2")
def task2_func(x,y):
    return x**2+y**2

result, error = dblquad(task2_func, 0,1,0,2)
print(f"∬(x²+y²) dxdy = {result}")
print(f"Погрешность: {error}")


# Задание 3:
# Найти площадь фигуры, ограниченной параболой y = x², осью x и прямыми x = 1, x = 3.
# Найти площадь фигуры, ограниченной линиями y = x и y = x² на отрезке [0, 1]. (Подсказка: нужно вычесть одну площадь из другой)
# Найти площадь полукруга радиусом 2 с помощью интеграла. Сравнить с формулой πR²/2.
print("Задание 3")
def task3_func(z,y,x):
    return z+y+x

result, error = tplquad(task3_func, 0,3,0,2,0,1)
print(f"∭(x+y+z) dxdydz = {result}")
print(F"Погрешность: {error}")


# Задание 4:
# Для подъёма груза на высоту h требуется сила F(h) = m·g·h, где m = 10 кг, g = 9.8. 
# Работа вычисляется как интеграл силы по высоте.
# Найти работу при подъёме груза с 0 до 5 метров.
# Найти работу при подъёме с 2 до 7 метров.
# Мощность электроприбора меняется по закону P(t) = 100 + 20·sin(t) (Вт). 
# Энергия = интеграл мощности по времени.
print("Задание 4")
def task4_func(x1,x2,x3,x4):
    return x1+2*x2+3*x3+4*x4

range = [(0,1),(0,1),(0,1),(0,1)]
result, error = nquad(task4_func, range)
print(f"(x1+2x2+3x3+4x4) dx1dx2dx3dx4 = {result}")
print(f"Погрешность: {error}")