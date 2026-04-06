import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, lagrange
from scipy.integrate import quad

# ЗАДАЧА 1. Интерполяция температуры
print("=" * 60)
print("ЗАДАЧА 1. Интерполяция температуры")
print("=" * 60)

x_temp = np.array([8, 10, 13, 16])
y_temp = np.array([15, 18, 22, 20])

# 1a. Полином Ньютона
def newton_poly(x_data, y_data):
    n = len(x_data)
    div_diff = y_data.copy()
    coeffs = [div_diff[0]]
    for j in range(1, n):
        for i in range(n - j):
            div_diff[i] = (div_diff[i + 1] - div_diff[i]) / (x_data[i + j] - x_data[i])
        coeffs.append(div_diff[0])
    
    def poly(x_val):
        res = coeffs[-1]
        for i in range(len(coeffs) - 2, -1, -1):
            res = res * (x_val - x_data[i]) + coeffs[i]
        return res
    return poly

newton_func = newton_poly(x_temp, y_temp)
points = [12, 14, 15.5]

print("\nа) Полином Ньютона:")
for t in points:
    temp_val = newton_func(t)
    print("   Время", t, ":00 -> Температура:", temp_val, "°C")

# 1b. Кубический сплайн
cs = CubicSpline(x_temp, y_temp)
print("\nб) Кубический сплайн:")
for t in points:
    temp_val = cs(t)
    print("   Время", t, ":00 -> Температура:", temp_val, "°C")

# График
x_smooth = np.linspace(7, 17, 300)
y_newton = []
for x in x_smooth:
    y_newton.append(newton_func(x))
y_spline = cs(x_smooth)

# plt.figure(figsize=(10, 4))
plt.plot(x_smooth, y_newton, label='Полином Ньютона')
plt.plot(x_smooth, y_spline, label='Кубический сплайн')
plt.scatter(x_temp, y_temp, color='red', zorder=5, label='Измерения')
plt.title('Задача 1: Интерполяция температуры')
plt.xlabel('Время (часы)')
plt.ylabel('Температура (°C)')
plt.legend()
plt.grid(True)
plt.show()

# Экстраполяция
print("\nЭкстраполяция на 9:00 и 17:00:")
for t in [9, 17]:
    val_n = newton_func(t)
    val_s = cs(t)
    print("   ", t, ":00 -> Ньютон:", val_n, "°C, Сплайн:", val_s, "°C")
print("Вывод: Сплайн надёжнее — полином Ньютона сильно колеблется на краях (эффект Рунге).")

# ЗАДАЧА 2. Феномен Рунге
print("\n" + "=" * 60)
print("ЗАДАЧА 2. Феномен Рунге")
print("=" * 60)

def runge_func(x):
    return 1 / (1 + 25 * x**2)

x_fine = np.linspace(-1, 1, 1000)
y_true = []
for x in x_fine:
    y_true.append(runge_func(x))
y_true = np.array(y_true)

# 6 узлов
x_nodes_6 = np.linspace(-1, 1, 6)
y_nodes_6 = []
for x in x_nodes_6:
    y_nodes_6.append(runge_func(x))
poly_6 = lagrange(x_nodes_6, y_nodes_6)

y_interp_6 = []
for x in x_fine:
    y_interp_6.append(poly_6(x))
y_interp_6 = np.array(y_interp_6)

error_6 = np.abs(y_interp_6 - y_true)
max_idx_6 = np.argmax(error_6)
print("а) 6 узлов. Максимальная погрешность =", error_6[max_idx_6], "в точке x =", x_fine[max_idx_6])

# 10 узлов
x_nodes_10 = np.linspace(-1, 1, 10)
y_nodes_10 = []
for x in x_nodes_10:
    y_nodes_10.append(runge_func(x))
poly_10 = lagrange(x_nodes_10, y_nodes_10)

y_interp_10 = []
for x in x_fine:
    y_interp_10.append(poly_10(x))
y_interp_10 = np.array(y_interp_10)

error_10 = np.abs(y_interp_10 - y_true)
max_idx_10 = np.argmax(error_10)
print("б) 10 узлов. Максимальная погрешность =", error_10[max_idx_10], "в точке x =", x_fine[max_idx_10])
print("   Увеличение числа узлов привело к резкому росту погрешности на краях.")
print("   Причина: феномен Рунге — осцилляции многочлена высокой степени.")

# График
# plt.figure(figsize=(10, 4))
plt.plot(x_fine, y_true, 'k-', label='Истинная функция')
plt.plot(x_fine, y_interp_6, 'b--', label='Интерполяция (6 узлов)')
plt.plot(x_fine, y_interp_10, 'r-.', label='Интерполяция (10 узлов)')
plt.scatter(x_nodes_6, y_nodes_6, color='blue', s=20)
plt.scatter(x_nodes_10, y_nodes_10, color='red', s=20)
plt.ylim(-1, 2)
plt.title('Задача 2: Феномен Рунге')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# ЗАДАЧА 3. Выбор метода для данных
print("\n" + "=" * 60)
print("ЗАДАЧА 3. Выбор метода для данных")
print("=" * 60)

print("а) Набор A (y = x*x) — идеально подходит полином 2-й степени, любой метод даст точный результат.")
print("б) Набор B (осцилляции 0/10) — глобальный полином Ньютона даст сильные выбросы. Лучше: кубические сплайны.")
print("в) Набор C (зашумлённые данные) — интерполяция через все точки плоха (переобучение).")

# Аппроксимация набора C
xC = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
yC = np.array([0.1, 0.9, 4.2, 8.8, 16.3, 24.1, 36.2, 49.3, 63.8, 80.1, 100.5])

coeffs = np.polyfit(xC, yC, 2)

def reg_poly(x):
    return coeffs[0] * x**2 + coeffs[1] * x + coeffs[2]

x_smooth_C = np.linspace(0, 10, 100)
y_reg_smooth = []
for x in x_smooth_C:
    y_reg_smooth.append(reg_poly(x))

# plt.figure(figsize=(8, 5))
plt.scatter(xC, yC, color='red', label='Зашумленные данные')
plt.plot(x_smooth_C, y_reg_smooth, 'g-', label='Регрессия (степень 2)')
plt.title('Задача 3в: Аппроксимация зашумленных данных')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

print("   Найденные коэффициенты регрессии: a =", coeffs[0], "b =", coeffs[1], "c =", coeffs[2])
print("   Это близко к y = 1*x*x + 0*x + 0")

# ============================================================
# ЧИСЛЕННОЕ ИНТЕГРИРОВАНИЕ
# ============================================================
print("\n" + "=" * 60)
print("ЧИСЛЕННОЕ ИНТЕГРИРОВАНИЕ")
print("=" * 60)

def left_rectangle(f, a, b, n):
    h = (b - a) / n
    x_vals = np.linspace(a, b - h, n)
    s = 0
    for x in x_vals:
        s = s + f(x)
    return s * h

# 1а. y = x*x на [0,2], n=4
def f1(x):
    return x * x

approx_1 = left_rectangle(f1, 0, 2, 4)

def exact_f1(x):
    return x**3 / 3
exact_1 = exact_f1(2) - exact_f1(0)

print("1а) Интеграл x*x от 0 до 2")
print("     Приближённо (левые прямоуг., n=4):", approx_1)
print("     Точное значение:", exact_1)
print("     Погрешность:", abs(exact_1 - approx_1))

# 1б. y = sin(x) на [0,pi], n=6
def f2(x):
    return np.sin(x)

approx_2 = left_rectangle(f2, 0, np.pi, 6)
exact_2, _ = quad(f2, 0, np.pi)

print("\n1б) Интеграл sin(x) от 0 до pi")
print("     Приближённо (левые прямоуг., n=6):", approx_2)
print("     Точное значение:", exact_2)
print("     Погрешность:", abs(exact_2 - approx_2))

# Задача 2. Реальная ситуация
print("\nЗадача 2. Реальная ситуация: расход топлива автомобиля")
print("Ситуация: Расход топлива (литров в час) меняется по закону r(t) = 5 + 3*sin(2*pi*t)")
print("Переменная t — часы с начала поездки (от 0 до 1).")

def fuel_rate(t):
    return 5 + 3 * np.sin(2 * np.pi * t)

total_fuel, _ = quad(fuel_rate, 0, 1)
print("Интеграл от 0 до 1 от (5 + 3*sin(2*pi*t)) dt =", total_fuel, "литров")
print("Смысл: За 1 час поездки автомобиль израсходует ровно 5 литров,")
print("так как вклад синуса за полный период обнуляется.")