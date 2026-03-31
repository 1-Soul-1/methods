import numpy as np
from scipy.interpolate import lagrange, KroghInterpolator
import matplotlib.pyplot as plt
import random


# Синус
# x = np.array([0,1,2,3,4,5,6])
# y = np.sin(x)
# x_lin = np.linspace(0,6,100)
# y_lin = np.interp(x_lin,x,y)

# plt.plot(x_lin,y_lin,'b-',label = "Линейная интерполяция")
# plt.plot(x,y,'ro', label = "Исходные точки")
# plt.legend()
# plt.grid(True)
# plt.show()


# Парабола
# x = np.array([0,1,2,3,4,5,])
# y = x**2 - 3*x + np.random.normal(0,0.5,6)

# x_lin = np.linspace(0,5,100)
# y_lin = np.interp(x_lin,x,y)

# plt.plot(x_lin,y_lin,'b-',label = "Линейная интерполяция")
# plt.plot(x,y,'ro', label = "Исходные точки")
# plt.legend()
# plt.grid(True)
# plt.show()


# Экспонента 
# x = np.array([1,2,3,4])
# y = np.exp(x/2)

# poly_lagrange = lagrange(x,y)
# poly_newton = KroghInterpolator(x,y)

# t = np.linspace(0,4,100)

# plt.plot(t,poly_lagrange(t),'b-', label = "Лагранж")
# plt.plot(t,poly_newton(t),'r--', label = "Ньютон")
# plt.plot(x,y,'go',markersize = 8)
# plt.legend()
# plt.show()


# # Ломанная
# x = np.array([0,1,2,3,4,5,6])
# y = np.array([1,5,2,9,3,8,4])

# x_lin = np.linspace(0,9,100)
# y_lin = np.interp(x_lin,x,y)

# plt.plot(x_lin,y_lin,'b-',label = "Линейная интерполяция")
# plt.plot(x,y,'ro', label = "Исходные точки")
# plt.legend()
# plt.grid(True)
# plt.show()


# # Затухание
# x = np.array([0,1,2,3,4,5,6,7])
# y = np.exp(-x/3)*np.cos(x**2)

# poly_lagrange = lagrange(x,y)
# poly_newton = KroghInterpolator(x,y)

# t = np.linspace(0,7,100)

# plt.plot(t,poly_lagrange(t),'b-', label = "Лагранж")
# plt.plot(t,poly_newton(t),'r--', label = "Ньютон")
# plt.plot(x,y,'go',markersize = 8)
# plt.legend()
# plt.show()