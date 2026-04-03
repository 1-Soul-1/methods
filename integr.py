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
def parabola(x):
    return x**2

result, error = quad(parabola, 0,2)
print(f"Парабола = {result}")
print(f"Погрешность параболы: {error}")

def line(x):
    return x*2

result, error = quad(line, 0,2)
print(f"Прямая = {result}")
print(f"Погрешность прямой: {error}")

def constant(x):
    return 5

result, error = quad(constant, 0,2)
print(f"Константа = {result}")
print(f"Погрешность константы: {error}")

def sine(x):
    return 5

result, error = quad(sine, 0,np.pi)
print(f"Константа = {result}")
print(f"Погрешность синуса: {error}")


# Задание 2:
# Скорость машины меняется по закону v(t) = t² + 2t + 1 (м/с).
# Какой путь проедет машина за 3 секунды?
# Какой путь проедет машина с 1-й по 3-ю секунду?
print("Задание 2")
def velocity(t):
    return t**2 + 2 * t + 1

result, error = quad(velocity, 0,3) 
print(f"Путь проедет машина за 3 секунды = {result}")

result, error = quad(velocity, 1,3) 
print(f"Путь c 1-й по 3-ю секунду = {result}")

# Задание 3:
# Найти площадь фигуры, ограниченной параболой y = x², осью x и прямыми x = 1, x = 3.
# Найти площадь фигуры, ограниченной линиями y = x и y = x² на отрезке [0, 1]. (Подсказка: нужно вычесть одну площадь из другой)
# Найти площадь полукруга радиусом 2 с помощью интеграла. Сравнить с формулой πR²/2.
print("Задание 3")
def parabola_area(x):
    return x**2

result, error = quad(parabola_area, 1,3)
print(f"Площадь фигуры 1 = {result}")

def parabola_area2(x):
    return x - x**2

result, error = quad(parabola_area2, 0,1)
print(f"Площадь фигуры 2 = {result}")

def semicircle(x):
    return np.sqrt(4-x**2)

result, error = quad(semicircle, -2,2)
area = np.pi*2**2/2
print(f"Площадь полукруга(интеграл) = {result}")
print(f"Площадь полукруга(формула) = {area}")
print(f"Разница = {result-area}")

# Задание 4:
# Для подъёма груза на высоту h требуется сила F(h) = m·g·h, где m = 10 кг, g = 9.8. 
# Работа вычисляется как интеграл силы по высоте.
# Найти работу при подъёме груза с 0 до 5 метров.
# Найти работу при подъёме с 2 до 7 метров.
# Мощность электроприбора меняется по закону P(t) = 100 + 20·sin(t) (Вт). 
# Энергия = интеграл мощности по времени.
print("Задание 4")
m,g = 10 , 9.8

def force(h):
    return m*g*h

result, error = quad(force, 0,5)
print(f"Работу при подъёме груза с 0 до 5 метров = {result}")
print(f"Погрешность: {error}")

def force2(h):
    return m*g*h

result, error = quad(force, 2,7)
print(f"Работу при подъёме груза с 2 до 7 метров = {result}")
print(f"Погрешность: {error}")

def power(t):
    return 100 + 20*np.sin(t)

result, error = quad(power, 0,2*np.pi)
print(f"Мощность = {result}")
print(f"Погрешность: {error}")