import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, lagrange
from scipy.integrate import quad

# ЗАДАЧА 1. Интерполяция температуры
print("ЗАДАЧА 1. Интерполяция температуры")

x_temp = np.array([8, 10, 13, 16])
y_temp = np.array([15, 18, 22, 20])

# a) Интерполяционный многочлен Ньютона
def newton_interpolation(x_data, y_data):
    n = len(x_data)
    coef = np.zeros([n, n])
    coef[:, 0] = y_data
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x_data[i+j] - x_data[i])      
    coeffs_newton = coef[0, :]
    
    def poly_newton(x_val):
        result = coeffs_newton[-1]
        for i in range(len(coeffs_newton) - 2, -1, -1):
            result = result * (x_val - x_data[i]) + coeffs_newton[i]
        return result 
    return poly_newton, coeffs_newton

poly_newton_func, coeffs = newton_interpolation(x_temp, y_temp)
print(f"Коэффициенты разделенных разностей (Ньютон): {coeffs}")

points_to_calc = [12, 14, 15.5] # 15:30 = 15.5
print("\nа) Значения температуры по Ньютону:")
for t in points_to_calc:
    temp_val = poly_newton_func(t)
    print(f"   Время {t}:00 -> Температура: {temp_val} °C")

# б) Кубический сплайн 
cs = CubicSpline(x_temp, y_temp)

print("\nб) Значения температуры по Кубическому Сплайну:")
for t in points_to_calc:
    temp_val = cs(t)
    print(f"   Время {t}:00 -> Температура: {temp_val} °C")

# Сравнение на графике
x_smooth = np.linspace(7, 17, 300)
y_newton = [poly_newton_func(x) for x in x_smooth]
y_spline = cs(x_smooth)

plt.figure()
plt.plot(x_smooth, y_newton, label='Полином Ньютона (Глобальный)')
plt.plot(x_smooth, y_spline, label='Кубический сплайн')
plt.scatter(x_temp, y_temp, color='red', zorder=5, label='Измерения')
plt.title('Задача 1: Интерполяция температуры')
plt.xlabel('Время (часы)')
plt.ylabel('Температура (°C)')
plt.legend()
plt.grid(True)
plt.show()

# Прогноз на 9:00 и 17:00 (экстраполяция)
t_extrap = [9, 17]
print("\nСравнение прогноза (экстраполяция):")
print(f"{'Время'} | {'Ньютон'} | {'Сплайн'}")
print("-" * 35)
for t in t_extrap:
    val_n = poly_newton_func(t)
    val_s = cs(t)
    print(f"{t}:00      | {val_n} | {val_s}")

print("\nВывод по Задаче 1 б:")
print("Для 9:00 и 17:00 (края диапазона) кубический сплайн обычно дает более правдоподобный результат,")
print("так как глобальный полином высокой степени склонен к сильным колебаниям (феномен Рунге) на краях.")
print("Сплайн же сохраняет гладкость и локальность изменений.")


# ЗАДАЧА 2. Феномен Рунге
print("ЗАДАЧА 2. Феномен Рунге")

def runge_func(x):
    return 1 / (1 + 25 * x**2)

x_fine = np.linspace(-1, 1, 1000)
y_true = runge_func(x_fine)

# а) 6 узлов
n_nodes_a = 6
x_nodes_a = np.linspace(-1, 1, n_nodes_a)
y_nodes_a = runge_func(x_nodes_a)

poly_lagrange_6 = lagrange(x_nodes_a, y_nodes_a)
y_interp_6 = poly_lagrange_6(x_fine)

error_6 = np.abs(y_interp_6 - y_true)
max_err_idx_6 = np.argmax(error_6)
max_err_x_6 = x_fine[max_err_idx_6]
max_err_val_6 = error_6[max_err_idx_6]

print(f"а) 6 узлов. Максимальная погрешность ≈ {max_err_val_6} в точке x ≈ {max_err_x_6}")

# б) 10 узлов
n_nodes_b = 10
x_nodes_b = np.linspace(-1, 1, n_nodes_b)
y_nodes_b = runge_func(x_nodes_b)

poly_lagrange_10 = lagrange(x_nodes_b, y_nodes_b)
y_interp_10 = poly_lagrange_10(x_fine)

error_10 = np.abs(y_interp_10 - y_true)
max_err_idx_10 = np.argmax(error_10)
max_err_x_10 = x_fine[max_err_idx_10]
max_err_val_10 = error_10[max_err_idx_10]

print(f"\nб) 10 узлов. Максимальная погрешность ≈ {max_err_val_10} в точке x ≈ {max_err_x_10}")
print("   Увеличение числа точек привело к РЕЗКОМУ росту погрешности на краях.")
print("   Причина: равноудаленные узлы для функций с особенностями в комплексной плоскости (как у Рунге)")
print("   вызывают осцилляции многочлена высокой степени на концах отрезка.")

# График феномена Рунге
plt.figure()
plt.plot(x_fine, y_true, 'k-', label='Истинная функция f(x)')
plt.plot(x_fine, y_interp_6, 'b--', label='Интерполяция (6 узлов)')
plt.plot(x_fine, y_interp_10, 'r-.', label='Интерполяция (10 узлов)')
plt.scatter(x_nodes_a, y_nodes_a, color='blue', s=20)
plt.scatter(x_nodes_b, y_nodes_b, color='red', s=20)
plt.ylim(-1, 2) # Ограничим ось Y, чтобы было видно колебания
plt.title('Задача 2: Феномен Рунге')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


# ЗАДАЧА 3. Выбор метода для данных
print("ЗАДАЧА 3. Выбор метода для данных")

# Набор A
xA = np.array([0, 1, 2, 3, 4, 5])
yA = np.array([0, 1, 4, 9, 16, 25])

# Набор B
xB = np.arange(0, 11)
yB = np.array([0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0])

# Набор C
xC = np.arange(0, 11)
yC = np.array([0.1, 0.9, 4.2, 8.8, 16.3, 24.1, 36.2, 49.3, 63.8, 80.1, 100.5])

print("а) Набор A: Данные точно описываются квадратичной функцией y=x^2.")
print("   Любой метод интерполяции даст точный результат, но достаточно полинома 2-й степени.")
print("   Метод наименьших квадратов (МНК) с степенью 2 восстановит формулу идеально.")

print("\nб) Набор B: Данные сильно осциллируют.")
print("   Многочлен Ньютона (глобальный полином 10-й степени) будет иметь огромные выбросы между узлами.")
print("   Лучше использовать: Кубические сплайны (они локальны) или тригонометрическую интерполяцию,")
print("   если природа данных периодическая.")

print("\nв) Набор C: Данные зашумлены.")
print("   Строить интерполяцию через ВСЕ точки нельзя — полином будет повторять шум (переобучение).")
print("   Альтернатива: Аппроксимация методом наименьших квадратов (регрессия).")
print("   Например,настроить параболу y = ax^2 + bx + c.")

coeffs_C_reg = np.polyfit(xC, yC, 2) # Квадратичная регрессия
poly_C_reg = np.poly1d(coeffs_C_reg)

x_smooth_C = np.linspace(0, 10, 100)
y_reg_smooth = poly_C_reg(x_smooth_C)

plt.figure()
plt.scatter(xC, yC, color='red', label='Зашумленные данные (C)')
plt.plot(x_smooth_C, y_reg_smooth, 'g-', label=f'Регрессия (степень 2): {poly_C_reg}')
plt.title('Задача 3в: Аппроксимация зашумленных данных')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

print(f"   Найденные коэффициенты регрессии для C: a={coeffs_C_reg[0]}, b={coeffs_C_reg[1]}, c={coeffs_C_reg[2]}")
print("   Это близко к y = 1*x^2 + 0*x + 0, что логично.")


# ЧИСЛЕННОЕ ИНТЕГРИРОВАНИЕ
print("ЧИСЛЕННОЕ ИНТЕГРИРОВАНИЕ")

# Задача 1. Площадь под кривой (метод прямоугольников)

def left_rectangle_rule(f, a, b, n):
    h = (b - a) / n
    x_vals = np.linspace(a, b - h, n)
    y_vals = f(x_vals)
    return np.sum(y_vals) * h

# а) y = x^2 на [0, 2], n=4
f1 = lambda x: x**2
area_approx_1 = left_rectangle_rule(f1, 0, 2, 4)
area_exact_1, _ = quad(f1, 0, 2)

print(f"Задача 1а: Интеграл x^2 от 0 до 2")
print(f"   Приближенно (левые прямоуг., n=4): {area_approx_1}")
print(f"   Точное значение: {area_exact_1}")
print(f"   Погрешность: {abs(area_exact_1 - area_approx_1)}")

# б) y = sin(x) на [0, pi], n=6
f2 = lambda x: np.sin(x)
area_approx_2 = left_rectangle_rule(f2, 0, np.pi, 6)
area_exact_2, _ = quad(f2, 0, np.pi)

print(f"\nЗадача 1б: Интеграл sin(x) от 0 до pi")
print(f"   Приближенно (левые прямоуг., n=6): {area_approx_2}")
print(f"   Точное значение: {area_exact_2}")
print(f"   Погрешность: {abs(area_exact_2 - area_approx_2)}")


# Задача 2. Реальная ситуация
print("Задача 2. Реальная ситуация: Расход топлива автомобиля")


# Расчет для ситуации
f_fuel = lambda t: 5 + 3 * np.sin(2 * np.pi * t)
fuel_total, _ = quad(f_fuel, 0, 1)
print(f"   Общий расход топлива: {fuel_total} литров.")