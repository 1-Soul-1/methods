# Численные методы
import numpy as np
from scipy.interpolate import lagrange, KroghInterpolator
import matplotlib.pyplot as plt
import random

# Интерполяция соединения точек прямыми
# Известные точки
# x = np.array([0,1,2,3,4])
# y = np.array([1,2,0,2,1])

# Линейная интерполяция(просто соединяем точки)
# x_lin = np.linspace(0,4,100)
# y_lin = np.interp(x_lin,x,y)

# plt.plot(x_lin,y_lin,'b-',label = "Линейная интерполяция")
# plt.plot(x,y,'ro', label = "Исходные точки")
# plt.legend()
# plt.grid(True)
# plt.show()


# Готовые методы Ньютона и Лагранжа - интреполяция из scipy
# Scipy - надстройка над numpy(научная библиотека для работы с тяжёлыми вычислительными данными)
# import numpy as np
# from scipy.interpolate import lagrange, KroghInterpolator
# import matplotlib.pyplot as plt

# x = np.array([0,1,2,3,4])
# y = np.array([1,2,0,2,1])

# # Метод Лагранжа в 1 строчку
# poly_lagrange = lagrange(x,y)

# # Метод Ньютона в 1 строчку
# poly_newton = KroghInterpolator(x,y)

# # Проверка 
# t = np.linspace(0,4,100)

# # Отрисовка
# plt.plot(t,poly_lagrange(t),'b-', label = "Лагранж")
# plt.plot(t,poly_newton(t),'r--', label = "Ньютон")
# plt.plot(x,y,'go',markersize = 8)
# plt.legend()
# plt.show()