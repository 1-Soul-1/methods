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

# Находим пределы для кадого Х
range = [(0,2),(0,2),(0,2),(0,2)]
result, error = nquad(nf, range)
print(result)